# Entrypoint: com.google.android.apps.chrome.firstrun.FirstRunActivity.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Landroid/app/Activity, startActivity(Landroid/content/Intent;)V >@120

IAAv10 = Int('IAAv10')    # Pointer<805177838>.this$0.mPrefManager.getFirstRunFlowSignInComplete()
IAAv0 = Real('IAAv0')    # <ChainedInput1>
IAAv13 = Int('IAAv13')    # Pointer<805177838>.this$0.mPrefManager.getFirstRunFlowSignInAccountName().isEmpty()
IAAv25 = Real('IAAv25')    # Pointer<805177838>.this$0.mActivity.get().mSignInObserver.val$observer
IAAv23 = Int('IAAv23')    # Pointer<805177838>.this$0.mActivity.get().mContext.get().hasSyncSetupCompleted()
IAAv16 = Real('IAAv16')    # Pointer<805177838>.this$0.mActivity.get().mSignInActivity
IAAv6 = Int('IAAv6')    # Pointer<805177838>.this$0.access$000()
IAAv17 = Real('IAAv17')    # Pointer<805177838>.this$0.mActivity.get().mSignInAccount
IAAv1 = Int('IAAv1')    # Pointer<582524242>.getBoolean()
IAAv2 = Int('IAAv2')    # Pointer<-1202501681>.getInstance().checkHasChildAccount().SDK_INT
IAAv22 = Int('IAAv22')    # Pointer<805177838>.this$0.mActivity.get().mContext.get().isSyncEnabled(Pointer<805177838>.this$0.mActivity.get().mSignInAccount)
IAAv3 = Real('IAAv3')    # Pointer<805177838>.mIsAndroidEduDevice
IAAv5 = Int('IAAv5')    # Pointer<805177838>.this$0.access$100()
IAAv15 = Int('IAAv15')    # Pointer<805177838>.this$0.mSignInType
IAAv26 = Int('IAAv26')    # Pointer<805177838>.this$0.mActivity.get().mSignInObserver.val$observer.this$0.access$400().getFirstRunFlowSignInSetupSync()
IAAv7 = Int('IAAv7')    # Pointer<805177838>.this$0.access$400().getFirstRunFlowComplete()
IAAv12 = Int('IAAv12')    # Pointer<805177838>.this$0.mActivity.getApplicationContext().get().isSignInAllowed()
IAAv27 = Int('IAAv27')    # Pointer<805177838>.this$0.mActivity.get().mSignInObserver.val$observer.this$0.access$500().get().getSignedInAccountName().isEmpty()
IAAv4 = Real('IAAv4')    # Pointer<805177838>.mHasChildAccount
IAAv14 = Real('IAAv14')    # Pointer<805177838>.this$0.mActivity.get().getAccountFromName(Pointer<805177838>.this$0.mPrefManager.getFirstRunFlowSignInAccountName())
IAAv18 = Real('IAAv18')    # Pointer<805177838>.this$0.mActivity.get().mSignInObserver
IAAv19 = Int('IAAv19')    # Pointer<805177838>.this$0.mActivity.get().mFirstRunCheckIsPending
IAAv24 = Int('IAAv24')    # Pointer<805177838>.this$0.mActivity.get().mSignInObserver.val$signInSync
IAAv8 = Int('IAAv8')    # Pointer<805177838>.this$0.access$400().getFirstRunFlowSignInComplete()
IAAv20 = Int('IAAv20')    # Pointer<805177838>.this$0.mActivity.get().nativeShouldLoadPolicyForUser(Pointer<805177838>.this$0.mActivity.get().getAccountFromName(Pointer<805177838>.this$0.mPrefManager.getFirstRunFlowSignInAccountName()).name)
IAAv9 = Int('IAAv9')    # Pointer<805177838>.this$0.access$200().onFirstRunCheckDone().$assertionsDisabled
IAAv11 = Int('IAAv11')    # Pointer<805177838>.this$0.mActivity.canAllowSync()
IAAv21 = Int('IAAv21')    # Pointer<805177838>.this$0.mActivity.get().notifySignInAllowedChanged().$assertionsDisabled

s.add(And(And(And(And(And(And(And(And(And(And(And(Or((IAAv0 == 0), (IAAv0 != 0)), (IAAv1 != 0)), (IAAv2 < 18)), And((IAAv3 != 0), (IAAv4 != 0))), And(And(Or(Or(And((IAAv5 == 0), (IAAv6 != 0)), And((IAAv5 == 0), (IAAv6 == 0))), (IAAv5 != 0)), (IAAv7 != 0)), (IAAv8 == 0))), And(And(And(And(Or((IAAv9 != 0), And((IAAv9 == 0), (IAAv10 == 0))), (IAAv11 != 0)), (IAAv12 != 0)), (IAAv13 == 0)), (IAAv14 != 0))), Or((IAAv15 == 0), (IAAv15 != 0))), And(And(Or((IAAv9 != 0), And(And(And((IAAv16 == 0), (IAAv17 == 0)), (IAAv9 == 0)), (IAAv18 == 0))), (IAAv19 == 0)), (IAAv20 == 0))), And(Or(Or(And(Or((IAAv21 != 0), And((IAAv21 == 0), (IAAv17 != 0))), (IAAv22 == 0)), And(And(Or((IAAv21 != 0), And((IAAv21 == 0), (IAAv17 != 0))), (IAAv22 != 0)), (IAAv23 != 0))), And(And(Or((IAAv21 != 0), And((IAAv21 == 0), (IAAv17 != 0))), (IAAv22 != 0)), (IAAv23 == 0))), (IAAv18 != 0))), And(Or((IAAv24 != 0), (IAAv24 == 0)), (IAAv25 != 0))), (IAAv26 != 0)), Or((IAAv27 != 0), (IAAv27 == 0))))

