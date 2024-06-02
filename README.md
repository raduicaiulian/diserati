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

# Generate CFG
In order to generate the CFG I'm working on 3 plans:

1. Attempted to use [this blog](https://clearbluejar.github.io/posts/callgraphs-with-ghidra-pyhidra-and-jpype/) to generate the CFG for a sample. Failed because I'm unable to instantiate monitor object, this [issue](https://github.com/dod-cyber-crime-center/pyhidra/issues/17) seemed related but did not helped. ~~It seems that it could be added by **add_classpaths**, but I'm not sure what is the java class that needs to be imported.(proved to be a false assumption).~~ It seems that it is provided by [`ghidra-stubs`](https://github.com/clearbluejar/ghidra-pyhidra-callgraphs/blob/77a013f360fae69b582bd75f6277ad8e43290545/requirements.txt#L1C1-L1C13)(see [L266](https://github.com/clearbluejar/ghidra-pyhidra-callgraphs/blob/77a013f360fae69b582bd75f6277ad8e43290545/ghidra_pyhidra_callgraphs.py#L266) and [L20](https://github.com/clearbluejar/ghidra-pyhidra-callgraphs/blob/77a013f360fae69b582bd75f6277ad8e43290545/ghidra_pyhidra_callgraphs.py#L20)).
2. Use [the gist](https://gist.github.com/bin2415/15028e78d5cf0c708fe1ab82fc252799) found by Ciprian
```
    set GHIDRA_PATH="C:\Users\%USERNAME%\Documents\ghidra_11.0.3_PUBLIC"
    set SCRIPT="ghidraCFG.py"
    set EXECUTABLE_TO_BE_ANALISED="Z:\samples_cgf\delete_sys32_file\delete_sys32_file.exe"
    set SCRIPT_PATH="C:\Users\%USERNAME%\Desktop\ghidra_script"

    %GHIDRA_PATH%\support\analyzeHeadless %TMP% TMP_PROJ -scriptPath %SCRIPT_PATH% -postScript %SCRIPT% -deleteProject -import %EXECUTABLE_TO_BE_ANALISED%
```

3. Play with Ghidra Script Manager, from what I see in the gist from the previous point, it looks like whatever script I craft, in theory, it should be easy to make it headless

# Familiarize with Analysis Options

* DWARF analyzer seems uselss for our porpouse (atm w'll focus on Windows only)
* go trough [this material|https://github.com/HackOvert/GhidraSnippets?tab=readme-ov-file#using-the-flatprogramapi], it gets you up to speed with the basics of flat Programing/Decompiler API + Complex API
* explore the functions from [here|https://github.com/NationalSecurityAgency/ghidra/issues/444]


# How to visualize dot files
1. [online tool](https://www.bing.com/ck/a?!&&p=7a3e2cd9e8160019JmltdHM9MTcxNzIwMDAwMCZpZ3VpZD0xYjRiODllNS1kZmVlLTYwN2MtMTY5NC05YTM4ZGUzNzYxNDgmaW5zaWQ9NTE5Ng&ptn=3&ver=2&hsh=3&fclid=1b4b89e5-dfee-607c-1694-9a38de376148&psq=dot+graph+viewer&u=a1aHR0cHM6Ly9kcmVhbXB1Zi5naXRodWIuaW8vR3JhcGh2aXpPbmxpbmUv&ntb=1)
2. Using dot program on linux(discovered by Mircea, not explored yet)



<!-- > [!NOTE] -->
> There is [also GhidraPAL](https://github.com/RolfRolles/GhidraPAL) which was referenced by some of the resources mentioned upward, but it lacks any kind of documentation, there is not even a simple instruction about how to use it so I gaved up on spending any thime on it.