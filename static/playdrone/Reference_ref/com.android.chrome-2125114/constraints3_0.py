# Entrypoint: com.google.android.apps.chrome.OpenDownloadReceiver.onReceive(Landroid/content/Context;Landroid/content/Intent;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@24

IAAv0 = Int('IAAv0')    # <Input2>.getAction()
IAAv1 = Int('IAAv1')    # equals9<return>

s.add(And((7000 != IAAv0), (IAAv1 == 0)))

