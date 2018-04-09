# Entrypoint: com.google.android.apps.chrome.ntp.RecentTabsPage.onChildClick(Landroid/widget/ExpandableListView;Landroid/view/View;IIJ)Z
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@22

IAAv2 = Real('IAAv2')    # Pointer<1405169743>.getGroup(<ChainedInput3>).getChild(<ChainedInput4>).getSnapshotViewableState()
IAAv0 = Real('IAAv0')    # Pointer<1405169743>.getGroup(<ChainedInput3>).getChild(<ChainedInput4>)
IAAv3 = Int('IAAv3')    # Pointer<-894397202>
IAAv1 = Int('IAAv1')    # Pointer<1405169743>.getGroup(<ChainedInput3>).getChild(<ChainedInput4>).isPrintedDocument()

s.add(And(And(And((IAAv0 != 0), (IAAv1 != 0)), (IAAv2 == IAAv3)), Or((IAAv1 == 0), (IAAv1 != 0))))

