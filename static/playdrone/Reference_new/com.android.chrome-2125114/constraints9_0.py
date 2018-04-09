# Entrypoint: com.google.android.apps.chrome.firstrun.FirstRunActivity.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Lcom/google/android/apps/chrome/firstrun/FirstRunActivity, startActivity(Landroid/content/Intent;)V >@139

IAAv0 = Real('IAAv0')    # <ChainedInput1>
IAAv1 = Int('IAAv1')    # Pointer<-320005533>.mResultSignInAccountName.isEmpty()
IAAv2 = Int('IAAv2')    # Pointer<-320005533>.mFreProperties.getBoolean()

s.add(And(Or((IAAv0 == 0), (IAAv0 != 0)), And(Or((IAAv1 != 0), (IAAv1 == 0)), (IAAv2 != 0))))

