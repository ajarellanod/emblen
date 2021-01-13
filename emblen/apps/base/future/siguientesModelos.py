class Cuenta(EmblenBaseModel):
    """Este modelo debería ir en otro Módulo, que debería ser donde se vayan a gestionar las Cuentas Bancarias - Tesorería"""
    
    banco = models.ForeignKey(
        Banco,
        related_name="cuentas",
        on_delete=models.PROTECT
    )

    numero = models.CharField(max_length=20)

    tipo =  models.ForeignKey(
        TipoCuenta,
        related_name="cuentas",
        on_delete=models.PROTECT
    )

    direccion = models.CharField(max_length=500)

    codigo_postal = models.CharField(max_length=5)

    telefono = models.CharField(max_length=13) #ej: 0414-419-6314

    correo = models.EmailField(max_length=254)

    repr_legal = models.CharField(max_length=100)

    rif_repr_legal = models.CharField(max_length=12)

    parroquia = models.ForeignKey(
        Parroquia,
        related_name="cuentas",
        on_delete=models.PROTECT
    )

    codigo_contable = models.ForeignKey(
        CodigoContable,
        related_name="Bancos",
        on_delete=models.PROTECT
    )

    saldo_ultima_conc = models.DecimalField(max_digits=22,decimal_places=4) 
    fecha_ultima_conc = models.DateField()

    saldo_conc_proceso = models.DecimalField(max_digits=22,decimal_places=4)
    fecha_conc_proceso = models.DateField()

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Cuentas Bancarias"