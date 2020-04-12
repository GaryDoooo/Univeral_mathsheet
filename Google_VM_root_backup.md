# To back up the google cloud vm / directory
# using 7z and tar to get maxium compression

7-zip doesn't preserve the Linux/Unix owner/group of files and possibly other details. Use tar instead because it's designed to preserve these things, then just 7zip the tar archive.

```
sudo tar cpf ericbackup.tar --exclude=/root --exclude=/proc --exclude=/lost+found --exclude=/ericbackup.tar --exclude=/var/lib/lxcfs --exclude=/mnt --exclude=/sys --exclude=/boot --exclude=/dev --exclude=/snap --exclude=/run --exclude=/tmp --exclude=/media --exclude=/.vifm* --exclude=/var/log --exclude=/home/du/tmp --exclude=/opt / 

7z a -t7z -m0=lzma2 -mx=9 -mfb=64 -md=32m -ms=on ericbackup.tar.7z /ericbackup.tar
```
To extract the archive:
```
7za x -so ericbackup.tar.7z  
tar xpf ericbackup.tar
```
