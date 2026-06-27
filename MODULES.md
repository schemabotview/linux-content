# Linux — module & section outline

The 10-module LFCS curriculum, every section, and the spine/depth tiering.
Source = the 10 runnable notebooks in `~/Projects/linux`. Goal: **lose no detail**
(every section becomes a page) while a curated **spine** drives feed mode.

## Tiering legend

- **★ spine** — essential; forms the narrated feed-mode story for the module.
- (plain) **depth** — kept as a page, explorable in canvas mode; not forced into the linear narration.
- *(no audio)* — a framing slide (What's covered / roadmap / What you've learned); a page with **no narration**.

Every section renders the single **`linux`** scene; the `highlight` column lists the
`lx-*` node ids that light AMBER for that section (see the node-id map at the end).

---

## 01 · Getting Started with Linux

- What's covered *(no audio)*
- ★ What is Linux? *(hook)* — `(full scene)`
- ★ Why Linux matters — `(full scene)`
- ★ Getting your own Linux to practise on — `(full scene)`
- ★ What you see when you log in — `lx-shell, lx-bash`
- ★ Your first commands — answering "where am I?" — `lx-shells`
- Listing what's in a directory — `ls` — `lx-shells, lx-fhs`
- ★ Moving around — `cd`, `..`, `.`, `~` — `lx-fhs, lx-vfs`
- Command structure — the anatomy of a command — `lx-shells`
- ★ A first tour of the filesystem hierarchy — `lx-fhs`
- Tab completion and history — the two shortcuts you'll use most — `lx-shell, lx-bash`
- Getting help — `man`, `--help`, `apropos`, `info` — `lx-shell`
- What you've learned *(no audio)*

## 02 · The Shell and Its Mechanics

- What's covered *(no audio)*
- A quick recap and where we're going *(no audio)*
- Keyboard shortcuts — the ones that pay back instantly *(hook)* — `lx-shell, lx-bash`
- ★ Variables — naming values — `lx-bash, lx-pvar`
- ★ The environment — variables that programs inherit — `lx-bash, lx-pvar`
- `export` — promoting a shell variable to the environment — `lx-pvar, lx-process`
- ★ Quoting — when the shell takes you literally — `lx-quote`
- ★ Output redirection — pointing the firehose — `lx-streams, lx-stdout, lx-stderr`
- Input redirection and here-documents — `lx-streams, lx-stdin`
- ★ Pipes — the most important character in the shell — `lx-streams, lx-stdout, lx-stdin`
- ★ Globs — matching filenames with patterns — `lx-glob`
- Expansion order — what the shell does to your line — `lx-expansion`
- What you've learned *(no audio)*

## 03 · Files, Folders & Permissions

- What's covered *(no audio)*
- Where we're going *(no audio)*
- ★ Creating files and directories — `touch` and `mkdir` *(hook)* — `lx-vfs, lx-inode`
- ★ Viewing file contents — `cat`, `less`, `head`, `tail`, `more` — `lx-vfs, lx-file`
- Copying — `cp` — `lx-vfs, lx-file`
- Moving and renaming — `mv` — `lx-vfs, lx-dentry`
- ★ Deleting — `rm` and the careful use of `rm -r` — `lx-vfs, lx-inode`
- ★ Links — hard links and symbolic links — `lx-hardlink, lx-symlink, lx-inode`
- The seven file types — `lx-vfs, lx-file`
- ★ The permissions model — who can do what — `lx-perms, lx-rwx`
- ★ Reading `ls -l` output, character by character — `lx-perms, lx-rwx`
- ★ `chmod` — changing permissions — `lx-rwx, lx-perms`
- ★ `chown` and `chgrp` — changing ownership — `lx-uid, lx-gid, lx-perms`
- `umask` — what new files get by default — `lx-rwx, lx-perms`
- Hidden files and dotfiles — `lx-fhs-home, lx-vfs`
- What you've learned *(no audio)*

## 04 · Text Processing & Find

- What's covered *(no audio)*
- ★ The Unix philosophy *(hook)* — `lx-shell, lx-streams`
- ★ `grep` — searching for text — `lx-shells`
- Regular expressions — the brief tour — `lx-shells`
- ★ `sed` — the stream editor — `lx-shells`
- ★ `awk` — the pattern-action language — `lx-shells`
- The supporting cast — `cut`, `sort`, `uniq` — `lx-streams`
- More supporting cast — `tr`, `wc`, `head`, `tail` — `lx-streams`
- ★ The "top-N by frequency" idiom — `lx-streams, lx-stdout`
- ★ `find` — searching the filesystem — `lx-vfs, lx-fhs`
- `find -exec` — acting on results — `lx-vfs`
- ★ Archives and compression — `tar` plus the lineup — `lx-block, lx-fs`
- The "tar pipe" idiom — `lx-streams, lx-ssh`
- What you've learned *(no audio)*

## 05 · Processes, Jobs & Signals

- What's covered *(no audio)*
- ★ What a process actually is *(hook)* — `lx-process, lx-fork`
- ★ `ps` — viewing processes — `lx-sched, lx-pid-table`
- `top` — the live view — `lx-sched, lx-cpu`
- `htop` — the friendlier alternative — `lx-sched, lx-cpu`
- ★ Process states — R, S, D, T, Z — `lx-sched, lx-runqueue`
- ★ Foreground vs background — `&`, `jobs`, `fg`, `bg` — `lx-process, lx-sched`
- Surviving session loss — `nohup`, `disown`, `setsid`, and `tmux` — `lx-process, lx-ssh`
- ★ Signals — the kernel's notification system — `lx-sigterm, lx-process`
- The signals you'll actually use — `lx-sigterm`
- ★ `kill`, `killall`, `pkill` — sending signals — `lx-sigterm, lx-process`
- The polite-then-forceful escalation — `lx-sigterm, lx-process`
- ★ Priority — `nice` and `renice` — `lx-nice, lx-runqueue, lx-sched`
- ★ Scheduled tasks — `cron` — `lx-process, lx-systemd`
- Other schedulers — `at` and systemd timers — `lx-systemd, lx-targets`
- What you've learned *(no audio)*

## 06 · Users, Groups & Access Control

- What's covered *(no audio)*
- ★ The Linux user model *(hook)* — `lx-users, lx-uid, lx-gid`
- ★ `/etc/passwd` — the user database — `lx-passwd, lx-uid, lx-fhs-etc`
- `/etc/shadow` — where passwords actually live — `lx-passwd, lx-fhs-etc`
- `/etc/group` — groups — `lx-gid, lx-fhs-etc`
- ★ User management — `useradd`, `usermod`, `userdel` — `lx-uid, lx-passwd`
- Passwords and account aging — `passwd`, `chage` — `lx-passwd`
- Group management — `groupadd`, `groupmod`, `groupdel`, `gpasswd` — `lx-gid`
- ★ Switching users — `su` vs `sudo` — `lx-sudo, lx-uid`
- `sudo` deep dive — `/etc/sudoers` and `visudo` — `lx-sudo, lx-fhs-etc`
- ★ Special permission bits — SUID, SGID, sticky — `lx-suid, lx-sgid, lx-perms`
- ★ ACLs — when standard owner/group/other isn't enough — `lx-acl, lx-perms`
- PAM — Pluggable Authentication Modules (preview) — `lx-perms, lx-fhs-etc`
- Shell startup files — which one runs when — `lx-shell, lx-bash, lx-fhs-home`
- What you've learned *(no audio)*

## 07 · Storage, Filesystems & Mounts

- What's covered *(no audio)*
- ★ The storage stack — a mental model *(hook)* — `lx-block, lx-fs, lx-blk`
- ★ Block devices and how Linux names them — `lx-blk, lx-disk, lx-fhs-dev`
- `lsblk` — see what's attached — `lx-blk, lx-block`
- Partitions and partition tables — MBR vs GPT — `lx-blk, lx-disk`
- ★ Filesystems — the layer that turns blocks into files — `lx-fs, lx-vfs`
- ★ Mounting — connecting filesystems to the tree — `lx-mount, lx-vfs, lx-fs`
- ★ `/etc/fstab` — persistent mounts — `lx-mount, lx-fhs-etc, lx-fs`
- UUID and LABEL — the stable way to identify filesystems — `lx-blk, lx-fs`
- `df` and `du` — the two questions about disk space — `lx-fs, lx-block`
- ★ Swap — virtual memory backup — `lx-swap, lx-mem, lx-disk`
- ★ LVM — flexible storage management — `lx-lvm, lx-blk`
- LVM operations — resize, snapshots, extend — `lx-lvm, lx-blk`
- RAID basics — redundancy across disks — `lx-raid, lx-blk`
- Quotas — per-user limits on disk usage — `lx-fs, lx-uid`
- What you've learned *(no audio)*

## 08 · Networking & SSH

- What's covered *(no audio)*
- ★ TCP/IP refresher *(hook)* — `lx-net, lx-tcp`
- ★ Network interfaces — `lx-net, lx-nic`
- ★ Getting an IP — static vs DHCP — `lx-net, lx-tcp`
- `nmcli` — NetworkManager from the command line — `lx-net, lx-tcp`
- ★ Routing — how packets find their destination — `lx-tcp, lx-netfilter, lx-net`
- ★ DNS — turning names into addresses — `lx-tcp, lx-fhs-etc`
- ★ SSH — the secure shell — `lx-ssh, lx-sockets`
- ★ SSH keys — the right way to authenticate — `lx-ssh`
- SSH config — `~/.ssh/config` — `lx-ssh, lx-fhs-home`
- `ssh-agent` and agent forwarding — `lx-ssh`
- ★ The SSH server — `sshd` and `/etc/ssh/sshd_config` — `lx-ssh, lx-sockets`
- File transfer — `scp` and `rsync` over SSH — `lx-ssh, lx-sockets`
- Firewalls — controlling what can reach you — `lx-netfilter, lx-tcp`
- ★ Network troubleshooting — ping, traceroute, ss — `lx-net, lx-tcp, lx-sockets`
- What you've learned *(no audio)*

## 09 · Services, Boot, systemd & Packages

- What's covered *(no audio)*
- ★ The boot sequence — power-on to login prompt *(hook)* — `lx-boot, lx-grub, lx-initramfs, lx-systemd`
- ★ What systemd is, in one minute — `lx-systemd, lx-units`
- Unit types — `lx-units, lx-systemd`
- ★ `systemctl` — the universal verb — `lx-systemd, lx-units`
- Reading `systemctl status` — `lx-systemd, lx-units`
- ★ Writing a basic service unit — `lx-units, lx-systemd`
- Drop-ins — modifying a vendor unit without editing it — `lx-units, lx-fhs-etc`
- ★ Targets — systemd's runlevels — `lx-targets, lx-systemd`
- ★ `journald` and `journalctl` — the systemd log system — `lx-journald`
- Traditional logs — `/var/log/` and `rsyslog` — `lx-journald, lx-fhs-var`
- ★ Package management — `apt` and `dnf` — `lx-pkg, lx-apt, lx-dnf`
- Repositories — where packages come from — `lx-pkg, lx-apt`
- What you've learned *(no audio)*

## 10 · Scripting, Troubleshooting & LFCS Prep

- What's covered *(no audio)*
- Why this final chapter exists *(no audio)*
- ★ Shell scripting essentials *(hook)* — `lx-shell, lx-bash`
- Conditionals — `if`, `test`, `[[ ]]` — `lx-bash`
- Loops — `for`, `while`, `until` — `lx-bash`
- ★ Functions, exit codes, and error handling — `lx-bash, lx-process`
- `set -euo pipefail` — the production-script preamble — `lx-bash`
- A complete example script — `lx-bash, lx-shells`
- ★ Troubleshooting methodology — `lx-trace, lx-journald`
- ★ Playbook 1 — disk is full — `lx-block, lx-fs, lx-fhs-var`
- ★ Playbook 2 — out of memory — `lx-oom, lx-mem, lx-swap`
- ★ Playbook 3 — runaway process pinning the CPU — `lx-sched, lx-cpu, lx-strace`
- ★ Playbook 4 — network is down — `lx-net, lx-tcp`
- ★ Playbook 5 — service won't start — `lx-systemd, lx-journald, lx-units`
- ★ Mandatory Access Control — SELinux and AppArmor — `lx-perms, lx-acl`
- Performance monitoring — `vmstat`, `iostat`, `sar` — `lx-trace, lx-perf, lx-cpu`
- ★ The LFCS exam — what to expect — `(full scene)`
- Exam strategy and tactics — `(full scene)`
- LFCS preparation checklist — `(full scene)`
- After LFCS — where to go next — `(full scene)`
- Closing the loop — the curriculum recap *(no audio)*

---

## Scene node-id map (`graphl-ux/src/data/scenes/linux.ts`)

The `linux` scene is the full stack. Highlight ids by band:

- **Shell / userspace (BLUE/YELLOW/TEAL):** `lx-shell`, `lx-shells` (`lx-bash`/`lx-dash`/`lx-ash`),
  `lx-expansion` (`lx-brace`/`lx-tilde`/`lx-pvar`/`lx-cmdsub`/`lx-arith`/`lx-split`/`lx-glob`/`lx-quote`),
  `lx-streams` (`lx-stdin`/`lx-stdout`/`lx-stderr`).
- **Process / users / perms (GREEN/PURPLE):** `lx-process` (`lx-fork`/`lx-exec`/`lx-wait`/`lx-exit`),
  `lx-users` (`lx-uid`/`lx-gid`/`lx-sudo`/`lx-passwd`), `lx-perms` (`lx-rwx`/`lx-suid`/`lx-sgid`/`lx-acl`).
- **Init / packages / boot (ORANGE/RED/GRAY):** `lx-systemd` (`lx-units`/`lx-targets`/`lx-journald`),
  `lx-pkg` (`lx-apt`/`lx-dnf`/`lx-apk`), `lx-boot` (`lx-grub`/`lx-initramfs`).
- **libc / syscall (YELLOW/RED):** `lx-libc` (`lx-glibc`/`lx-musl`),
  `lx-syscall` (`lx-open`/`lx-read`/`lx-write`/`lx-mmap`/`lx-ioctl`/`lx-execve`).
- **Kernel (GREEN/BLUE/PURPLE/TEAL/ORANGE/GRAY):** `lx-vfs` (`lx-inode`/`lx-dentry`/`lx-file`/`lx-mount`/`lx-hardlink`/`lx-symlink`),
  `lx-sched` (`lx-pid-table`/`lx-runqueue`/`lx-nice`/`lx-sigterm`), `lx-mem` (`lx-mmu`/`lx-page-cache`/`lx-swap`/`lx-oom`),
  `lx-block` (`lx-fs`/`lx-blk`/`lx-lvm`/`lx-raid`), `lx-net` (`lx-sockets`/`lx-tcp`/`lx-netfilter`/`lx-ssh`),
  `lx-trace` (`lx-strace`/`lx-perf`/`lx-ebpf`).
- **Containers (RED):** `lx-ns` (`lx-ns-pid`/`lx-ns-net`/`lx-ns-mnt`/`lx-ns-user`/`lx-ns-uts`/`lx-ns-ipc`),
  `lx-cgroups` (`lx-cg-cpu`/`lx-cg-mem`/`lx-cg-io`).
- **Filesystem view (GRAY):** `lx-fhs-proc`/`lx-fhs-sys`/`lx-fhs-dev`/`lx-fhs-etc`/`lx-fhs-var`/`lx-fhs-home`/`lx-fhs-tmp`/`lx-fhs-run`.
- **Hardware (PURPLE/BLUE/TEAL/ORANGE):** `lx-cpu`/`lx-ram`/`lx-disk`/`lx-nic`.
