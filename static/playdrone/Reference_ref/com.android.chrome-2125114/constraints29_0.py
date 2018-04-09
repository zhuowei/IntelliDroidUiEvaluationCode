# Entrypoint: org.chromium.chrome.browser.WebsiteSettingsPopup.onClick(Landroid/view/View;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@145

IAAv1 = Real('IAAv1')    # <ChainedInput1>
IAAv0 = Int('IAAv0')    # Pointer<-1287734171>
IAAv3 = Int('IAAv3')    # Pointer<954506152>
IAAv2 = Int('IAAv2')    # Pointer<1364166028>

s.add(And(And((IAAv0 != IAAv1), (IAAv2 != IAAv1)), (IAAv3 == IAAv1)))

