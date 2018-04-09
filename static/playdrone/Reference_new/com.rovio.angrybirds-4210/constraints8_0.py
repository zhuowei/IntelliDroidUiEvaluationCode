# Entrypoint: com.rovio.skynest.socialnetwork.SocialSharingViewWrapper.onResume()V
# Target: invokevirtual < Application, Landroid/app/Activity, startActivityForResult(Landroid/content/Intent;I)V >@9

IAAv2 = Real('IAAv2')    # Pointer<1464921565>.getSocialServiceForName().d.b
IAAv1 = Real('IAAv1')    # Pointer<1464921565>.getSocialServiceForName().d
IAAv0 = Real('IAAv0')    # Pointer<1464921565>.getSocialServiceForName()

s.add(And(And((IAAv0 != 0), (IAAv1 != 0)), Or((IAAv2 == 0), (IAAv2 != 0))))

