# Entrypoint: com.google.android.apps.chrome.promoscreen.DataReductionPromoScreen.onClick(Landroid/view/View;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@85

IAAv1 = Int('IAAv1')    # Pointer<-373268461>
IAAv2 = Int('IAAv2')    # Pointer<-1361925629>
IAAv0 = Int('IAAv0')    # <ChainedInput1>.getId()

s.add(And((IAAv0 != IAAv1), (IAAv0 == IAAv2)))

