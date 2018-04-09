# Entrypoint: android.support.v7.widget.ActivityChooserView$Callbacks.onItemClick(Landroid/widget/AdapterView;Landroid/view/View;IJ)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@229

IAAv2 = Int('IAAv2')    # Pointer<218430246>.mAdapter.getShowDefaultActivity()
IAAv0 = Int('IAAv0')    # <ChainedInput1>.getAdapter().getItemViewType()
IAAv1 = Int('IAAv1')    # Pointer<218430246>.mIsSelectingDefaultActivity
IAAv3 = Real('IAAv3')    # Pointer<218430246>.mAdapter.getDataModel().chooseActivity((<ChainedInput3> + 1) | <Input3>)

s.add(And(Or(And(And((IAAv0 == 0), (IAAv1 == 0)), (IAAv2 == 0)), And(And((IAAv0 == 0), (IAAv1 == 0)), (IAAv2 != 0))), (IAAv3 != 0)))

