# Entrypoint: com.google.android.apps.books.app.UploadsActivityAlias$1.onClick(Landroid/content/DialogInterface;I)V
# Target: invokevirtual < Application, Lcom/google/android/apps/books/app/UploadsActivityAlias, startActivity(Landroid/content/Intent;)V >@138

IAAv2 = BitVec('IAAv2',32)    # Pointer<-1927690418>.getMaxUploadSizeMB()
IAAv0 = Int('IAAv0')    # Pointer<-1927690418>.isDeviceConnected()
IAAv3 = Int('IAAv3')    # Pointer<-1927690418>.downloadContentSilently()
IAAv4 = Real('IAAv4')    # Pointer<-1927690418>.getUploadsController()
IAAv1 = BitVec('IAAv1',32)    # Pointer<-1027899409>.getFileSize(Pointer<-1927690418>.getContentResolver())

s.add(And(And(And((IAAv0 != 0), (IAAv1 <= (1048576 * IAAv2))), (IAAv3 != 0)), Or((IAAv4 == 0), (IAAv4 != 0))))

