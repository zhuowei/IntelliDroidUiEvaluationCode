# Entrypoint: android.support.v7.widget.ActivityChooserView$Callbacks.onClick(Landroid/view/View;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@140

IAAv0 = Real('IAAv0')    # <ChainedInput1>
IAAv2 = Real('IAAv2')    # Pointer<218430246>.mAdapter.getDataModel().chooseActivity(Pointer<218430246>.mAdapter.getDataModel().getActivityIndex(Pointer<218430246>.mAdapter.getDefaultActivity()))
IAAv1 = Real('IAAv1')    # Pointer<218430246>.mDefaultActivityButton

s.add(And((IAAv0 == IAAv1), (IAAv2 != 0)))

