# Entrypoint: org.chromium.chrome.browser.banners.AppBannerView.onClick(Landroid/view/View;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@238

IAAv1 = Real('IAAv1')    # <ChainedInput1>
IAAv3 = Int('IAAv3')    # Pointer<1575947283>
IAAv0 = Int('IAAv0')    # Pointer<493222995>
IAAv2 = Int('IAAv2')    # Pointer<-275476451>

s.add(And(And(And(And((IAAv0 != 0), (IAAv1 == IAAv2)), (IAAv3 != 1)), (IAAv3 != 0)), (IAAv3 == 2)))

