# Entrypoint: com.fsck.k9.activity.Accounts.onItemClick(Landroid/widget/AdapterView;Landroid/view/View;IJ)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@12

IAAv1 = Int('IAAv1')    # <Input1>.getItemAtPosition().isAvailable()
IAAv2 = Int('IAAv2')    # <Input1>.getItemAtPosition().getAutoExpandFolderName()
IAAv0 = Int('IAAv0')    # <Input1>.getItemAtPosition().isEnabled()
IAAv3 = Int('IAAv3')    # equals16<return>

s.add(And(And(And((IAAv0 != 0), (IAAv1 != 0)), And((7000 == IAAv2), (IAAv3 == 1))), (IAAv3 != 0)))

