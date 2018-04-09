# Entrypoint: com.google.android.apps.chrome.prerender.PrerenderAPITestActivity.onClick(Landroid/view/View;)V
# Target: invokevirtual < Application, Lcom/google/android/apps/chrome/prerender/PrerenderAPITestActivity, startActivity(Landroid/content/Intent;)V >@124

IAAv0 = Int('IAAv0')    # <ChainedInput1>.getId()
IAAv2 = Int('IAAv2')    # Pointer<295593550>
IAAv1 = Int('IAAv1')    # Pointer<-1024317499>

s.add(And((IAAv0 != IAAv1), (IAAv0 == IAAv2)))

