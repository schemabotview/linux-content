#!/usr/bin/env python3
"""Build manifest.json for linux-content from the notebooks + a curated overlay.

Every notebook '## ' heading becomes a section (a slide). Content sections (those
with a matching tts/<NN>-<SS>-*.tts) get scene+spine+highlight+audio; framing
sections (What's covered / roadmap / What you've learned) are slides with no audio.
SS = the notebook section's 1-based order, which is also the tts stem's SS.
"""
import json, re, glob, os

NB_DIR = "/Users/maddipotiganesh/Products/linux-content/notebooks"
TTS_DIR = "/Users/maddipotiganesh/Products/linux-content/tts"
OUT = "/Users/maddipotiganesh/Products/linux-content/manifest.json"

TITLES = {
    "01": "Getting Started with Linux",
    "02": "The Shell and Its Mechanics",
    "03": "Files, Folders & Permissions",
    "04": "Text Processing & Find",
    "05": "Processes, Jobs & Signals",
    "06": "Users, Groups & Access Control",
    "07": "Storage, Filesystems & Mounts",
    "08": "Networking & SSH",
    "09": "Services, Boot, systemd & Packages",
    "10": "Scripting, Troubleshooting & LFCS Prep",
}
PID = {
    "01": "01-getting-started", "02": "02-shell-mechanics",
    "03": "03-files-permissions", "04": "04-text-processing",
    "05": "05-processes-signals", "06": "06-users-access-control",
    "07": "07-storage-filesystems", "08": "08-networking-ssh",
    "09": "09-services-systemd", "10": "10-scripting-lfcs",
}

# Per-section highlight (lx-* node ids from graphl-ux src/data/scenes/linux.ts),
# keyed by tts stem. Empty list => full-strength scene (used for module hooks).
HL = {
 # module 01
 "01-02-what-is-linux": [], "01-03-why-linux-matters": [],
 "01-04-getting-your-own-linux": [], "01-05-what-you-see-when-you-log-in": ["lx-shell","lx-bash"],
 "01-06-your-first-commands": ["lx-shells"], "01-07-listing-a-directory": ["lx-shells","lx-fhs"],
 "01-08-moving-around": ["lx-fhs","lx-vfs"], "01-09-command-structure": ["lx-shells"],
 "01-10-filesystem-hierarchy": ["lx-fhs"], "01-11-tab-completion-and-history": ["lx-shell","lx-bash"],
 "01-12-getting-help": ["lx-shell"],
 # module 02
 "02-03-keyboard-shortcuts": ["lx-shell","lx-bash"], "02-04-variables": ["lx-bash","lx-pvar"],
 "02-05-the-environment": ["lx-bash","lx-pvar"], "02-06-export": ["lx-pvar","lx-process"],
 "02-07-quoting": ["lx-quote"], "02-08-output-redirection": ["lx-streams","lx-stdout","lx-stderr"],
 "02-09-input-redirection": ["lx-streams","lx-stdin"], "02-10-pipes": ["lx-streams","lx-stdout","lx-stdin"],
 "02-11-globs": ["lx-glob"], "02-12-expansion-order": ["lx-expansion"],
 # module 03
 "03-03-creating-files-and-directories": ["lx-vfs","lx-inode"], "03-04-viewing-file-contents": ["lx-vfs","lx-file"],
 "03-05-copying": ["lx-vfs","lx-file"], "03-06-moving-and-renaming": ["lx-vfs","lx-dentry"],
 "03-07-deleting": ["lx-vfs","lx-inode"], "03-08-links": ["lx-hardlink","lx-symlink","lx-inode"],
 "03-09-seven-file-types": ["lx-vfs","lx-file"], "03-10-permissions-model": ["lx-perms","lx-rwx"],
 "03-11-reading-ls-l": ["lx-perms","lx-rwx"], "03-12-chmod": ["lx-rwx","lx-perms"],
 "03-13-chown-and-chgrp": ["lx-uid","lx-gid","lx-perms"], "03-14-umask": ["lx-rwx","lx-perms"],
 "03-15-hidden-files": ["lx-fhs-home","lx-vfs"],
 # module 04
 "04-02-unix-philosophy": ["lx-shell","lx-streams"], "04-03-grep": ["lx-shells"],
 "04-04-regular-expressions": ["lx-shells"], "04-05-sed": ["lx-shells"], "04-06-awk": ["lx-shells"],
 "04-07-cut-sort-uniq": ["lx-streams"], "04-08-tr-wc-head-tail": ["lx-streams"],
 "04-09-top-n-by-frequency": ["lx-streams","lx-stdout"], "04-10-find": ["lx-vfs","lx-fhs"],
 "04-11-find-exec": ["lx-vfs"], "04-12-archives-and-compression": ["lx-block","lx-fs"],
 "04-13-tar-pipe": ["lx-streams","lx-ssh"],
 # module 05
 "05-02-what-a-process-is": ["lx-process","lx-fork"], "05-03-ps": ["lx-sched","lx-pid-table"],
 "05-04-top": ["lx-sched","lx-cpu"], "05-05-htop": ["lx-sched","lx-cpu"],
 "05-06-process-states": ["lx-sched","lx-runqueue"], "05-07-foreground-vs-background": ["lx-process","lx-sched"],
 "05-08-surviving-session-loss": ["lx-process","lx-ssh"], "05-09-signals": ["lx-sigterm","lx-process"],
 "05-10-the-signals-you-will-use": ["lx-sigterm"], "05-11-kill-killall-pkill": ["lx-sigterm","lx-process"],
 "05-12-escalation": ["lx-sigterm","lx-process"], "05-13-priority-nice-renice": ["lx-nice","lx-runqueue","lx-sched"],
 "05-14-cron": ["lx-process","lx-systemd"], "05-15-other-schedulers": ["lx-systemd","lx-targets"],
 # module 06
 "06-02-user-model": ["lx-users","lx-uid","lx-gid"], "06-03-etc-passwd": ["lx-passwd","lx-uid","lx-fhs-etc"],
 "06-04-etc-shadow": ["lx-passwd","lx-fhs-etc"], "06-05-etc-group": ["lx-gid","lx-fhs-etc"],
 "06-06-user-management": ["lx-uid","lx-passwd"], "06-07-passwords-and-aging": ["lx-passwd"],
 "06-08-group-management": ["lx-gid"], "06-09-su-vs-sudo": ["lx-sudo","lx-uid"],
 "06-10-sudoers-visudo": ["lx-sudo","lx-fhs-etc"], "06-11-special-permission-bits": ["lx-suid","lx-sgid","lx-perms"],
 "06-12-acls": ["lx-acl","lx-perms"], "06-13-pam": ["lx-perms","lx-fhs-etc"],
 "06-14-shell-startup-files": ["lx-shell","lx-bash","lx-fhs-home"],
 # module 07
 "07-02-storage-stack": ["lx-block","lx-fs","lx-blk"], "07-03-block-devices": ["lx-blk","lx-disk","lx-fhs-dev"],
 "07-04-lsblk": ["lx-blk","lx-block"], "07-05-partitions": ["lx-blk","lx-disk"],
 "07-06-filesystems": ["lx-fs","lx-vfs"], "07-07-mounting": ["lx-mount","lx-vfs","lx-fs"],
 "07-08-fstab": ["lx-mount","lx-fhs-etc","lx-fs"], "07-09-uuid-and-label": ["lx-blk","lx-fs"],
 "07-10-df-and-du": ["lx-fs","lx-block"], "07-11-swap": ["lx-swap","lx-mem","lx-disk"],
 "07-12-lvm": ["lx-lvm","lx-blk"], "07-13-lvm-operations": ["lx-lvm","lx-blk"],
 "07-14-raid-basics": ["lx-raid","lx-blk"], "07-15-quotas": ["lx-fs","lx-uid"],
 # module 08
 "08-02-tcp-ip-refresher": ["lx-net","lx-tcp"], "08-03-network-interfaces": ["lx-net","lx-nic"],
 "08-04-getting-an-ip": ["lx-net","lx-tcp"], "08-05-nmcli": ["lx-net","lx-tcp"],
 "08-06-routing": ["lx-tcp","lx-netfilter","lx-net"], "08-07-dns": ["lx-tcp","lx-fhs-etc"],
 "08-08-ssh": ["lx-ssh","lx-sockets"], "08-09-ssh-keys": ["lx-ssh"],
 "08-10-ssh-config": ["lx-ssh","lx-fhs-home"], "08-11-ssh-agent": ["lx-ssh"],
 "08-12-ssh-server": ["lx-ssh","lx-sockets"], "08-13-file-transfer": ["lx-ssh","lx-sockets"],
 "08-14-firewalls": ["lx-netfilter","lx-tcp"], "08-15-network-troubleshooting": ["lx-net","lx-tcp","lx-sockets"],
 # module 09
 "09-02-boot-sequence": ["lx-boot","lx-grub","lx-initramfs","lx-systemd"], "09-03-what-systemd-is": ["lx-systemd","lx-units"],
 "09-04-unit-types": ["lx-units","lx-systemd"], "09-05-systemctl": ["lx-systemd","lx-units"],
 "09-06-reading-systemctl-status": ["lx-systemd","lx-units"], "09-07-writing-a-service-unit": ["lx-units","lx-systemd"],
 "09-08-drop-ins": ["lx-units","lx-fhs-etc"], "09-09-targets": ["lx-targets","lx-systemd"],
 "09-10-journald-journalctl": ["lx-journald"], "09-11-traditional-logs": ["lx-journald","lx-fhs-var"],
 "09-12-package-management": ["lx-pkg","lx-apt","lx-dnf"], "09-13-repositories": ["lx-pkg","lx-apt"],
 # module 10
 "10-03-shell-scripting-essentials": ["lx-shell","lx-bash"], "10-04-conditionals": ["lx-bash"],
 "10-05-loops": ["lx-bash"], "10-06-functions-exit-codes": ["lx-bash","lx-process"],
 "10-07-set-euo-pipefail": ["lx-bash"], "10-08-complete-example-script": ["lx-bash","lx-shells"],
 "10-09-troubleshooting-methodology": ["lx-trace","lx-journald"], "10-10-playbook-disk-full": ["lx-block","lx-fs","lx-fhs-var"],
 "10-11-playbook-out-of-memory": ["lx-oom","lx-mem","lx-swap"], "10-12-playbook-runaway-cpu": ["lx-sched","lx-cpu","lx-strace"],
 "10-13-playbook-network-down": ["lx-net","lx-tcp"], "10-14-playbook-service-wont-start": ["lx-systemd","lx-journald","lx-units"],
 "10-15-mandatory-access-control": ["lx-perms","lx-acl"], "10-16-performance-monitoring": ["lx-trace","lx-perf","lx-cpu"],
 "10-17-lfcs-exam": [], "10-18-exam-strategy": [], "10-19-lfcs-prep-checklist": [], "10-20-after-lfcs": [],
}

# Depth (spine=false) sections: reference-heavy, kept as pages but off the feed spine.
DEPTH = {
 "01-07-listing-a-directory","01-09-command-structure","01-11-tab-completion-and-history","01-12-getting-help",
 "02-03-keyboard-shortcuts","02-06-export","02-09-input-redirection","02-12-expansion-order",
 "03-05-copying","03-06-moving-and-renaming","03-09-seven-file-types","03-14-umask","03-15-hidden-files",
 "04-04-regular-expressions","04-07-cut-sort-uniq","04-08-tr-wc-head-tail","04-11-find-exec","04-13-tar-pipe",
 "05-04-top","05-05-htop","05-08-surviving-session-loss","05-10-the-signals-you-will-use","05-12-escalation","05-15-other-schedulers",
 "06-04-etc-shadow","06-05-etc-group","06-07-passwords-and-aging","06-08-group-management","06-10-sudoers-visudo","06-13-pam","06-14-shell-startup-files",
 "07-04-lsblk","07-05-partitions","07-09-uuid-and-label","07-10-df-and-du","07-13-lvm-operations","07-14-raid-basics","07-15-quotas",
 "08-05-nmcli","08-10-ssh-config","08-11-ssh-agent","08-13-file-transfer","08-14-firewalls",
 "09-04-unit-types","09-06-reading-systemctl-status","09-08-drop-ins","09-11-traditional-logs","09-13-repositories",
 "10-04-conditionals","10-05-loops","10-07-set-euo-pipefail","10-08-complete-example-script",
 "10-16-performance-monitoring","10-18-exam-strategy","10-19-lfcs-prep-checklist","10-20-after-lfcs",
}

def headings(path):
    """Every '## ' heading line, in order — matches how the app splits sections."""
    nb = json.load(open(path))
    out = []
    for c in nb["cells"]:
        if c["cell_type"] != "markdown":
            continue
        for line in "".join(c["source"]).split("\n"):
            m = re.match(r"^##\s+(?!#)(.+)", line.strip())
            if m:
                out.append(m.group(1).strip())
    return out

presentations = []
for nb_path in sorted(glob.glob(f"{NB_DIR}/*.ipynb")):
    nb_file = os.path.basename(nb_path)
    nn = nb_file[:2]
    hs = headings(nb_path)
    # tts stems present for this module, keyed by SS (int)
    stems = {}
    for t in glob.glob(f"{TTS_DIR}/{nn}-*.tts"):
        stem = os.path.basename(t)[:-4]
        ss = int(stem.split("-")[1])
        stems[ss] = stem
    sections = []
    first_content = True
    for i, h in enumerate(hs, start=1):
        sec = {"heading": h, "scene": "linux", "spine": False}
        stem = stems.get(i)
        if stem:  # content section -> audio + highlight (+ hook on the first)
            sec["spine"] = stem not in DEPTH
            if first_content:
                sec["role"] = "hook"
                first_content = False
            hl = HL.get(stem, [])
            if hl:
                sec["highlight"] = hl
            sec["audio"] = f"audio/{stem}.wav"
        sections.append(sec)
    presentations.append({
        "id": PID[nn],
        "title": TITLES[nn],
        "notebook": f"notebooks/{nb_file}",
        "defaultScene": "linux",
        "sections": sections,
    })

manifest = {
    "concept": "Linux",
    "design": "DESIGN.md",
    "scenes": [
        {"id": "linux", "title": "Linux — the full stack (userspace → kernel → hardware)", "status": "built"}
    ],
    "presentations": presentations,
}
with open(OUT, "w") as f:
    json.dump(manifest, f, indent=2)
    f.write("\n")

tot = sum(len(p["sections"]) for p in presentations)
aud = sum(1 for p in presentations for s in p["sections"] if "audio" in s)
print(f"wrote {OUT}: {len(presentations)} presentations, {tot} sections, {aud} with audio")
