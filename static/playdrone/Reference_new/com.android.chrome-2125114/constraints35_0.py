# Entrypoint: com.google.android.apps.chrome.firstrun.FirstRunActivity.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Landroid/widget/ExpandableListView, setOnChildClickListener(Landroid/widget/ExpandableListView$OnChildClickListener;)V >@141

IAAv11 = Int('IAAv11')    # Pointer<805177838>.this$0.mPrefManager.getFirstRunFlowSignInComplete()
IAAv0 = Real('IAAv0')    # <ChainedInput1>
IAAv14 = Int('IAAv14')    # Pointer<805177838>.this$0.mPrefManager.getFirstRunFlowSignInAccountName().isEmpty()
IAAv24 = Int('IAAv24')    # Pointer<-1614051752>
IAAv25 = Real('IAAv25')    # Pointer<805177838>.this$0.mPrefManager.setFirstRunFlowSignInComplete().$SwitchMap$com$google$android$apps$chrome$tab$NativePageFactory$NativePageType
IAAv6 = Int('IAAv6')    # Pointer<805177838>.this$0.access$000()
IAAv23 = Int('IAAv23')    # Pointer<805177838>.this$0.mObserver.this$0.getTabCreator().mTabModel.indexOf()
IAAv1 = Int('IAAv1')    # Pointer<582524242>.getBoolean()
IAAv16 = Int('IAAv16')    # Pointer<805177838>.this$0.mObserver.val$firstRunToSignIn
IAAv8 = Int('IAAv8')    # Pointer<805177838>.this$0.access$500().checkAnyUserHasSeenToS()
IAAv2 = Int('IAAv2')    # Pointer<-1202501681>.getInstance().checkHasChildAccount().SDK_INT
IAAv3 = Real('IAAv3')    # Pointer<805177838>.mIsAndroidEduDevice
IAAv5 = Int('IAAv5')    # Pointer<805177838>.this$0.access$100()
IAAv22 = Int('IAAv22')    # Pointer<805177838>.this$0.mObserver.this$0.getTabModelSelector().getModel().getTabIndexByUrl()
IAAv7 = Int('IAAv7')    # Pointer<805177838>.this$0.access$400().getFirstRunFlowComplete()
IAAv19 = Int('IAAv19')    # Pointer<805177838>.this$0.mObserver.this$0.getTabModelSelector().getModel().getCurrentTab().getUrl()
IAAv18 = Real('IAAv18')    # Pointer<805177838>.this$0.mObserver.this$0.getTabModelSelector().getModel().getCurrentTab()
IAAv13 = Int('IAAv13')    # Pointer<805177838>.this$0.mActivity.getApplicationContext().get().isSignInAllowed()
IAAv4 = Real('IAAv4')    # Pointer<805177838>.mHasChildAccount
IAAv20 = Int('IAAv20')    # equals15<return>
IAAv9 = Int('IAAv9')    # Pointer<805177838>.this$0.access$400().getFirstRunFlowSignInComplete()
IAAv21 = Int('IAAv21')    # Pointer<805177838>.this$0.mObserver.this$0.mTabModelSelectorImpl.tryToRestoreTabState()
IAAv10 = Int('IAAv10')    # Pointer<805177838>.this$0.access$200().onFirstRunCheckDone().$assertionsDisabled
IAAv12 = Int('IAAv12')    # Pointer<805177838>.this$0.mActivity.canAllowSync()
IAAv15 = Real('IAAv15')    # Pointer<805177838>.this$0.mObserver
IAAv17 = Int('IAAv17')    # Pointer<805177838>.this$0.mObserver.this$0.access$000().getRestoredTabCount()

s.add(And(And(And(And(And(And(And(And(And(And(Or((IAAv0 == 0), Not((IAAv0 == 0))), (IAAv1 != 0)), Not((IAAv2 >= 18))), And(Not((IAAv3 == 0)), (IAAv4 != 0))), And(And(Or(And(Or(Or(And((IAAv5 == 0), Not((IAAv6 == 0))), And((IAAv5 == 0), (IAAv6 == 0))), Not((IAAv5 == 0))), (IAAv7 != 0)), And(And(Or(Or(And((IAAv5 == 0), Not((IAAv6 == 0))), And((IAAv5 == 0), (IAAv6 == 0))), Not((IAAv5 == 0))), Not((IAAv7 != 0))), (IAAv8 == 0))), (IAAv7 != 0)), Not((IAAv9 != 0)))), And(Or(Or(And(Or((IAAv10 != 0), And(Not((IAAv10 != 0)), (IAAv11 == 0))), (IAAv12 == 0)), And(And(Or((IAAv10 != 0), And(Not((IAAv10 != 0)), (IAAv11 == 0))), Not((IAAv12 == 0))), (IAAv13 == 0))), And(And(And(Or((IAAv10 != 0), And(Not((IAAv10 != 0)), (IAAv11 == 0))), Not((IAAv12 == 0))), Not((IAAv13 == 0))), Not((IAAv14 == 0)))), Not((IAAv15 == 0)))), And(Not((IAAv16 == 0)), Not((IAAv17 != 0)))), And(And(Or((IAAv18 == 0), And(And(Not((IAAv18 == 0)), Or(And((7000 == IAAv19), (IAAv20 == 1)), And((7000 != IAAv19), (IAAv20 == 0)))), (IAAv20 == 0))), Not((IAAv21 != 0))), (IAAv22 == -1))), Not((IAAv23 == -1))), Not((IAAv24 != 0))), (IAAv25 == 5)))

