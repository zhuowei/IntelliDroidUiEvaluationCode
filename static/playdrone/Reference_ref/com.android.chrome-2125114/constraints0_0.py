# Entrypoint: com.google.android.apps.chrome.appwidget.bookmarks.BookmarkWidgetProxy.onReceive(Landroid/content/Context;Landroid/content/Intent;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@12

IAAv1 = Int('IAAv1')    # <Input2>.getAction()
IAAv2 = Int('IAAv2')    # equals10<return>
IAAv0 = Int('IAAv0')    # <Input1>.getChangeFolderAction()

s.add(And((IAAv0 != IAAv1), (IAAv2 == 0)))

