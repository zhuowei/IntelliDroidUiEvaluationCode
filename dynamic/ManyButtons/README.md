## ManyButtons demo

### Using IntelliDroid: Static:

Check out and build GUI branch, then

`./runStaticOnManyButtons.sh`

time: On i5-4210Y

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

### Using Sapienz:

todo:

### Using Monkey:

todo:
