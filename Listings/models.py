from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .accounts import ListingsUserManager

accounts = (
    ("customer", "Customer"),
    ("agent", "Agent"),
    ('admin', 'Admin')
)

class ListingsUser(AbstractBaseUser, PermissionsMixin):
    class FcAccountType:
        CUSTOMER = accounts[0][0]
        AGENT = accounts[1][0]
        ADMIN = accounts[2][0]

    REQUIRED_FIELDS = ['email']

    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=255, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    account_type = models.CharField(_('Account Type'), default='customer', max_length=500, choices=accounts)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_superuser = models.BooleanField(_('super status'), default=False,
                                       help_text=_('Designates whether the user can log into this admin '
                                                   'site.'))
    is_active = models.BooleanField(_('active'), default=False,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = ListingsUserManager()

    class Meta:
        db_table = "Listings_user"
        verbose_name = _("User")
    
        def __str__(self):
            return self.email

        def get_user_type(self):
            return self.account_type
        
        def get_full_name(self):
            """User full name"""
            return f"{self.first_name} {self.last_name}"
