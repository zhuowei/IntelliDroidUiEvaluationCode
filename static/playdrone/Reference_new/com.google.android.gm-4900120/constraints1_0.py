# Entrypoint: com.google.android.gm.ComposeActivityGmail.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Lcom/android/mail/compose/g, startActivityForResult(Landroid/content/Intent;I)V >@80

IAAv0 = Real('IAAv0')    # <Input1>

s.add(Or((IAAv0 == 0), (IAAv0 != 0)))

