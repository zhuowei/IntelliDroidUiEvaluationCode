# Entrypoint: com.fsck.k9.ui.messageview.MessageContainerView.onCreateContextMenu(Landroid/view/ContextMenu;Landroid/view/View;Landroid/view/ContextMenu$ContextMenuInfo;)V
# Target: invokeinterface < Application, Landroid/view/MenuItem, setOnMenuItemClickListener(Landroid/view/MenuItem$OnMenuItemClickListener;)Landroid/view/MenuItem; >@620

IAAv0 = Int('IAAv0')    # <Input2>.getHitTestResult().getType()
IAAv1 = Real('IAAv1')    # <Input2>.getHitTestResult().getExtra().parse()

s.add(And((IAAv0 == 5), Not((IAAv1 == 0))))

