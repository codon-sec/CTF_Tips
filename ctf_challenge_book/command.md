### sysytem striction
# !/bin/bash
apt-get install -y git

# x86バイナリを動かす為のパッケージ
dpkg --add-architecture i386
apt-get update
apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386
apt-get install gcc-multilib g++-multilib

# radare2
git clone https://github.com/radare/radare2
sh radare2/sys/install.sh

# ELF解析用
apt-get install binutils
 
# ROPガジェット用
wget https://github.com/0vercl0k/rp/releases/download/v1/rp-lin-x64 \
&& wget https://github.com/0vercl0k/rp/releases/download/v1/rp-lin-x86 \
&& chmod +x rp-lin-x64 rp-lin-x86 \
&& mv rp-lin-x64 rp-lin-x86 /usr/local/bint
