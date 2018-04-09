# Entrypoint: com.google.android.apps.chrome.OpenDownloadReceiver.onReceive(Landroid/content/Context;Landroid/content/Intent;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@146

IAAv0 = Int('IAAv0')    # <Input2>.getAction()
IAAv1 = Int('IAAv1')    # equals9<return>
IAAv2 = Real('IAAv2')    # <Input2>.getLongArrayExtra()
IAAv3 = Real('IAAv3')    # <Input1>.getSystemService().getUriForDownloadedFile()

s.add(And(And(And(And((7000 == IAAv0), (IAAv1 == 1)), (IAAv1 != 0)), (IAAv2 != 0)), (IAAv3 != 0)))

