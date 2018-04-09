## ManyButtons demo

### Using IntelliDroid: Static:

Check out and build GUI branch, then

`./runStaticOnManyButtons.sh`

time: On i5-4210Y, Ubuntu 14.04

```
real	0m42.745s
user	1m15.337s
sys	0m2.656s
```

Output is in `out`; Sample output in `Reference_out`

### Dynamic:

Use an API19 emulator (Sapienz needs it, we use it so we can compare)

I'm using the API19 Google APIs x86 emulator, with the default Nexus 5 config.
 name the AVD `avd19_0`, and clear the AVD data in Android Studio prior to each use.

`./installDynamic.sh`
`time ./runDynamicOnManyButtons.sh`

time: on i7-5500U, Ubuntu 16.04

```
time ./runDynamicOnManyButtons.sh 
Looking for Android device and IntelliDroidService...
Connected to IntelliDroidService
WARNING: linker: libdvm.so has text relocations. This is wasting memory and is a security risk. Please fix.
WARNING: linker: libdvm.so has text relocations. This is wasting memory and is a security risk. Please fix.
> > {'extras': 'listenerFieldName:mOnClickListener inListenerInfo:true', 'type': u'onClick', 'input:id': '2130968612'}
WARNING: linker: libdvm.so has text relocations. This is wasting memory and is a security risk. Please fix.
WARNING: linker: libdvm.so has text relocations. This is wasting memory and is a security risk. Please fix.
WARNING: linker: libdvm.so has text relocations. This is wasting memory and is a security risk. Please fix.
> 
real	0m8.204s
user	0m0.304s
sys	0m0.071s
```

### Using Sapienz:

todo:

### Using Monkey:

todo:
