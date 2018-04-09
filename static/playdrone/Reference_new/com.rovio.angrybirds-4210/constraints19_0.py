# Entrypoint: com.mopub.mobileads.cq.onTouch(Landroid/view/View;Landroid/view/MotionEvent;)Z
# Target: invokevirtual < Application, Lcom/mopub/mobileads/MraidVideoPlayerActivity, startActivityForResult(Landroid/content/Intent;I)V >@18

IAAv1 = Int('IAAv1')    # Pointer<1219251658>.a()
IAAv0 = Int('IAAv0')    # <ChainedInput2>.getAction()

s.add(And((IAAv0 == 1), (IAAv1 != 0)))

