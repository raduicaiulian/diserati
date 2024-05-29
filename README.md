# Create environment
1. Download the VM from [osboxex website](https://www.osboxes.org/debian/), I used the one with **57c6f93f1250ae7e1538358a838b682a95bf97fb2d36160b4d8c8354e9d8a24f** SHA256 hash;
2. Unzip the image(`$ 7z e 64bit.7z`) and import the VDI file in Virtual Media Manager of VirtualBox, the attach it to a new VM;
3. Optional steps:
    1. Disable root password(`passwd -d root`);
    2. Install VirtualBox addition pack in order to be able to change the resolution;
    3. map shared directory to facilitate easy file transfer access between host and guest;

# Install ghidra
1. Download the ghidra from [github releases](https://github.com/NationalSecurityAgency/ghidra/releases) page and unzip it, I used the one with **2462a2d0ab11e30f9e907cd3b4aa6b48dd2642f325617e3d922c28e752be6761** SHA256 hash.
2. Install java(`apt install openjdk-17-jdk`);