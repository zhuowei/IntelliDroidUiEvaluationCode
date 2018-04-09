# Entrypoint: com.google.android.apps.chrome.preferences.Preferences.onHeaderClick(Landroid/preference/PreferenceActivity$Header;I)V
# Target: invokevirtual < Application, Landroid/app/AlertDialog$Builder, setPositiveButton(ILandroid/content/DialogInterface$OnClickListener;)Landroid/app/AlertDialog$Builder; >@32

IAAv3 = BitVec('IAAv3',32)    # Pointer<735319699>
IAAv4 = BitVec('IAAv4',32)    # Pointer<-2019120988>
IAAv2 = BitVec('IAAv2',32)    # Pointer<-78356796>
IAAv1 = BitVec('IAAv1',32)    # Pointer<-1482351225>
IAAv0 = BitVec('IAAv0',32)    # <ChainedInput1>.id

s.add(And(Or(And(Or(And(Or(Or((IAAv0 != IAAv1), Not((IAAv0 != IAAv1))), Not((IAAv0 != IAAv1))), (IAAv0 != IAAv2)), And(Or(Or((IAAv0 != IAAv1), Not((IAAv0 != IAAv1))), Not((IAAv0 != IAAv1))), Not((IAAv0 != IAAv2)))), (IAAv0 != IAAv3)), And(Or(And(Or(Or((IAAv0 != IAAv1), Not((IAAv0 != IAAv1))), Not((IAAv0 != IAAv1))), (IAAv0 != IAAv2)), And(Or(Or((IAAv0 != IAAv1), Not((IAAv0 != IAAv1))), Not((IAAv0 != IAAv1))), Not((IAAv0 != IAAv2)))), Not((IAAv0 != IAAv3)))), Not((IAAv0 != IAAv4))))

