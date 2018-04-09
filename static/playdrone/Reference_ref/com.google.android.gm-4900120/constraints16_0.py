# Entrypoint: com.google.android.gm.photo.GmailPhotoViewActivity.onClick(Landroid/view/View;)V
# Target: invokevirtual < Application, Lcom/google/android/gm/photo/GmailPhotoViewActivity, startActivity(Landroid/content/Intent;)V >@37

IAAv0 = Int('IAAv0')    # <ChainedInput1>.getId()
IAAv1 = Int('IAAv1')    # Pointer<-1013779076>

s.add(And((IAAv0 == 2131427649), (IAAv1 != 0)))

