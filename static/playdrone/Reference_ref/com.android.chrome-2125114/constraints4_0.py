# Entrypoint: com.google.android.apps.chrome.sync.ui.SyncCustomizationFragment.onResume()V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@105

IAAv3 = Real('IAAv3')    # Pointer<1346342848>.getResult()
IAAv4 = Int('IAAv4')    # Pointer<1346342848>.getResult().containsKey()
IAAv2 = Int('IAAv2')    # Pointer<1251687914>.mProfileSyncService.isSyncInitialized()
IAAv0 = Int('IAAv0')    # Pointer<-278850307>.setSetupInProgress().$assertionsDisabled
IAAv1 = Int('IAAv1')    # Pointer<1251687914>.mDestroyed

s.add(And(And(Or((IAAv0 != 0), And((IAAv0 == 0), (IAAv1 == 0))), (IAAv2 == 0)), And((IAAv3 != 0), (IAAv4 != 0))))

