# Entrypoint: com.google.android.gms.ads.AdActivity.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Lcom/google/android/gms/internal/dd, setDownloadListener(Landroid/webkit/DownloadListener;)V >@145

IAAv3 = Int('IAAv3')    # Pointer<-761422368>.nd.setContentView(Pointer<-761422368>.nn).SDK_INT
IAAv0 = Int('IAAv0')    # Pointer<-761422368>
IAAv1 = Int('IAAv1')    # Pointer<-761422368>.ne.nA
IAAv2 = Int('IAAv2')    # Pointer<-761422368>.setRequestedOrientation(Pointer<-761422368>.ne.orientation).SDK_INT

s.add(And(And(And((IAAv0 != 0), (IAAv1 == 1)), Or((IAAv2 < 11), Not((IAAv2 < 11)))), Or(Or(And((IAAv3 < 17), (IAAv3 < 11)), And((IAAv3 < 17), Not((IAAv3 < 11)))), Not((IAAv3 < 17)))))

