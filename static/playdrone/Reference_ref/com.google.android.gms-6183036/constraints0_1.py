# Entrypoint: com.google.android.location.network.ConfirmAlertActivity.onClick(Landroid/content/DialogInterface;I)V
# Target: invokevirtual < Application, Lcom/google/android/location/network/ConfirmAlertActivity, startActivity(Landroid/content/Intent;)V >@76

IAAv0 = Int('IAAv0')    # <ChainedInput2>
IAAv1 = Int('IAAv1')    # Pointer<-1925798733>

s.add(And(Or((IAAv0 != -1), (IAAv0 == -1)), (IAAv1 != 0)))

