from django.db import models
from wagtail.core.models import Page
from customblocks import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
#from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailyoast.edit_handlers import YoastPanel
from wagtail.search import index
import requests
import random
from django.contrib.auth import get_user_model
from wagtail.users.models import UserProfile
from manjaro.settings.base import MEDIA_ROOT, MEDIA_URL

# pre defined pages 

class Downloads(Page):
    max_count=1
    template = "home/downloads.html"
    subpage_types = []
    parent_page_types = [
        'home.HomePage'
    ]

    intro = models.TextField(default='', blank=True, max_length=350)

    question_one = models.CharField(default='', blank=True, max_length=50)
    answer_one = models.TextField(default='', blank=True, max_length=200)

    question_two = models.CharField(default='', blank=True, max_length=50)
    answer_two = models.TextField(default='', blank=True, max_length=200)

    question_three = models.CharField(default='', blank=True, max_length=50)
    answer_three = models.TextField(default='', blank=True, max_length=200)

    team_spins_intro = models.TextField(default='', blank=True, max_length=200)
    community_spins_intro = models.TextField(default='', blank=True, max_length=200)
    arm_spins_intro = models.TextField(default='', blank=True, max_length=200)
    manual_intro = models.TextField(default='', blank=True, max_length=200)
    docker_intro = models.TextField(default='', blank=True, max_length=200)

    xfce_description = models.TextField(default='', blank=True, max_length=150)
    xfce_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    xfce_notes = models.TextField(default='', blank=True, max_length=200)

    plasma_description = models.TextField(default='', blank=True, max_length=150)
    plasma_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    plasma_notes = models.TextField(default='', blank=True, max_length=200)

    gnome_description = models.TextField(default='', blank=True, max_length=150)
    gnome_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    gnome_notes = models.TextField(default='', blank=True, max_length=200)

    cinnamon_description = models.TextField(default='', blank=True, max_length=150)
    cinnamon_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    cinnamon_notes = models.TextField(default='', blank=True, max_length=200)

    i3_description = models.TextField(default='', blank=True, max_length=150)
    i3_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    i3_notes = models.TextField(default='', blank=True, max_length=200)

    budgie_description = models.TextField(default='', blank=True, max_length=150)
    budgie_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    budgie_notes = models.TextField(default='', blank=True, max_length=200)

    mate_description = models.TextField(default='', blank=True, max_length=150)
    mate_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    mate_notes = models.TextField(default='', blank=True, max_length=200)

    sway_description = models.TextField(default='', blank=True, max_length=150)
    sway_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    sway_notes = models.TextField(default='', blank=True, max_length=200)


    edition_panels = [
        FieldPanel("xfce_description"),
        #ImageChooserPanel('xfce_image'),
        FieldPanel("xfce_notes"),
        FieldPanel("plasma_description"),
        #ImageChooserPanel('plasma_image'),
        FieldPanel("plasma_notes"),
        FieldPanel("gnome_description"),
        #ImageChooserPanel('gnome_image'),
        FieldPanel("gnome_notes"),

        FieldPanel("cinnamon_description"),
        #ImageChooserPanel('cinnamon_image'),
        FieldPanel("cinnamon_notes"),
        FieldPanel("budgie_description"),
        #ImageChooserPanel('budgie_image'),
        FieldPanel("budgie_notes"),
        FieldPanel("i3_description"),
        #ImageChooserPanel('i3_image'),
        FieldPanel("i3_notes"),
        FieldPanel("mate_description"),
        #ImageChooserPanel('mate_image'),
        FieldPanel("mate_notes"),
        FieldPanel("sway_description"),
        #ImageChooserPanel('sway_image'),
        FieldPanel("sway_notes"),
    ]
    

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("question_one"),
        FieldPanel("answer_one"),
        FieldPanel("question_two"),
        FieldPanel("answer_two"),
        FieldPanel("question_three"),
        FieldPanel("answer_three"),
        FieldPanel("team_spins_intro"),
        FieldPanel("community_spins_intro"),
        FieldPanel("arm_spins_intro"),
        FieldPanel("manual_intro"),
        FieldPanel("docker_intro"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("question_one"),
        index.SearchField("answer_one"),
        index.SearchField("question_two"),
        index.SearchField("answer_two"),
        index.SearchField("question_three"),
        index.SearchField("answer_three"),
        index.SearchField("team_spins_intro"),
        index.SearchField("community_spins_intro"),
        index.SearchField("arm_spins_intro"),
        index.SearchField("manual_intro"),
        index.SearchField("docker_intro")
    ]
    

    def get_context(self, request):
        data_source = "https://gitlab.manjaro.org/webpage/iso-info/-/raw/master/file-info.json"
        response = requests.get(data_source)
        data = response.json()

        context = super(Downloads, self).get_context(request)
        context['data'] = data
        return context


    keywords = models.CharField(default='', blank=True, max_length=100)

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(edition_panels, heading=('Editions')),
        ObjectList(Page.promote_panels, heading=('Promote')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ])

#Downloads._meta.get_field("title").default = "Downloads"
#Downloads._meta.get_field("slug").default = "default-homepage-title"


class Donations(Page):
    max_count=1
    template = "home/donations.html"
    subpage_types = []
    parent_page_types = [
        'home.HomePage'
    ]

    intro = models.TextField(max_length=350, null=True)

    content = StreamField(
        [
            ("richtext", blocks.RichtextBlock()),
        ],
        null=True,
        blank=True,
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('content'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel("content"),
    ]

    keywords = models.CharField(default='', blank=True, max_length=150)

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(Page.promote_panels, heading=('Promote')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ])  


class Hardware(Page):
    max_count=1
    template = "home/hardware.html"
    subpage_types = []
    parent_page_types = [
        'home.HomePage'
    ]

    intro = models.TextField(max_length=350, null=True)

    content = StreamField(
        [
            ("product_details", blocks.ProductBlock()),        
        ],
        null=True,
        blank=True,
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('content'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel("content"),
    ]

    keywords = models.CharField(default='', blank=True, max_length=150)

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(Page.promote_panels, heading=('Promote')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ])


#Donations._meta.get_field("title").default = "Donations"
#Donations._meta.get_field("slug").default = "default-homepage-title"

class Features(Page):
    max_count=1
    template = "home/features.html"
    subpage_types = []
    parent_page_types = [
        'home.HomePage'
    ]

    intro =  models.TextField(blank=True, max_length=450)
    branches_intro =  models.TextField(blank=True, max_length=650)
    arch_linux_intro =  models.TextField(blank=True, max_length=350)
    unstable_intro =  models.TextField(blank=True, max_length=350)
    testing_intro =  models.TextField(blank=True, max_length=350)
    stable_intro =  models.TextField(blank=True, max_length=350)

    pamac_intro =  models.TextField(blank=True, max_length=350)
    package_formats_intro =  models.TextField(blank=True, max_length=350)
    updates_intro =  models.TextField(blank=True, max_length=350)
    aur_intro =  models.TextField(blank=True, max_length=450)

    gnome_layout_switcher_intro =  models.TextField(blank=True, max_length=350)
    manjaro_layout_intro =  models.TextField(blank=True, max_length=350)
    traditional_layout_intro =  models.TextField(blank=True, max_length=350)
    tilling_layout_intro =  models.TextField(blank=True, max_length=350)
    gnome_layout_intro =  models.TextField(blank=True, max_length=350)

    msm_intro =  models.TextField(blank=True, max_length=350)
    kernels_intro =  models.TextField(blank=True, max_length=350)
    common_settings_intro =  models.TextField(blank=True, max_length=350)
    graphic_drivers_intro =  models.TextField(blank=True, max_length=350)

    web_app_manager_intro =  models.TextField(blank=True, max_length=450)
    microsoft_office_intro =  models.TextField(blank=True, max_length=350)
    skype_intro =  models.TextField(blank=True, max_length=350)

    calamares_intro =  models.TextField(blank=True, max_length=450)    

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField("branches_intro"),
        index.SearchField("arch_linux_intro"),
        index.SearchField("unstable_intro"),
        index.SearchField("testing_intro"),
        index.SearchField("stable_intro"),
        index.SearchField("pamac_intro"),
        index.SearchField("package_formats_intro"),
        index.SearchField("updates_intro"),
        index.SearchField("aur_intro"),
        index.SearchField("gnome_layout_switcher_intro"),
        index.SearchField("manjaro_layout_intro"),
        index.SearchField("traditional_layout_intro"),
        index.SearchField("tilling_layout_intro"),
        index.SearchField("gnome_layout_intro"),
        index.SearchField("msm_intro"),
        index.SearchField("kernels_intro"),
        index.SearchField("common_settings_intro"),
        index.SearchField("graphic_drivers_intro"),
        index.SearchField("web_app_manager_intro"),
        index.SearchField("microsoft_office_intro"),
        index.SearchField("skype_intro"),
        index.SearchField("calamares_intro"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("branches_intro"),
        FieldPanel("arch_linux_intro"),
        FieldPanel("unstable_intro"),
        FieldPanel("testing_intro"),
        FieldPanel("stable_intro"),
        FieldPanel("pamac_intro"),
        FieldPanel("package_formats_intro"),
        FieldPanel("updates_intro"),
        FieldPanel("aur_intro"),
        FieldPanel("gnome_layout_switcher_intro"),
        FieldPanel("manjaro_layout_intro"),
        FieldPanel("traditional_layout_intro"),
        FieldPanel("tilling_layout_intro"),
        FieldPanel("gnome_layout_intro"),
        FieldPanel("msm_intro"),
        FieldPanel("kernels_intro"),
        FieldPanel("common_settings_intro"),
        FieldPanel("graphic_drivers_intro"),
        FieldPanel("web_app_manager_intro"),
        FieldPanel("microsoft_office_intro"),
        FieldPanel("skype_intro"),
        FieldPanel("calamares_intro"),
    ]

    keywords = models.CharField(default='', blank=True, max_length=150)

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(Page.promote_panels, heading=('Promote')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ])


class Team(Page):
    max_count=1
    title = "Team"
    template = "home/team.html"
    subpage_types = []
    parent_page_types = [
        'home.HomePage'
    ]

    intro =  models.TextField(blank=True, max_length=350)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        User = get_user_model()
        users = User.objects.all()
        profiles =[]
        for user in users:
            profile = UserProfile.get_for_user(user)
            name = profile.user.get_full_name()
            title = profile.user.title
            description = profile.user.description
            try:
                avatar = f"/media/{profile.user.avatar.file}"
            except AttributeError:
                imgs =["jaro-1.png", "jaro-3.png"]
                avatar = f"/static/img/{random.choice(imgs)}"
            tweeter = profile.user.tweeter
            github = profile.user.github
            dict = {"name": name, "title": title, "description": description, "avatar": avatar, "tweeter": tweeter, "github": github}
            profiles.append(dict) 
           
        context = super().get_context(request)
        context['users'] = profiles
        return context

    keywords = models.CharField(default='', blank=True, max_length=150)

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(Page.promote_panels, heading=('Promote')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ]) 

#Team._meta.get_field("title").default = "Team"
#Team._meta.get_field("slug").default = "default-homepage-title"

# end pre defined pages 

class CustomPage(Page):
    template = "home/custom-page.html"
    subpage_types = []
    parent_page_types = [
        'home.HomePage'
    ]

    intro =  models.TextField(default='', blank=True, max_length=350)

    content = StreamField(
        [
            ("richtext", blocks.RichtextBlock()),
        ],
        null=True,
        blank=True,
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('content'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        StreamFieldPanel("content"),
    ]
    

    keywords = models.CharField(default='', blank=True, max_length=150)

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(Page.promote_panels, heading=('Promote')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ])


class PartnersSponsors(Page):
    max_count=2
    template = "home/partners-sponsors.html"
    subpage_types = []
    parent_page_types = [
        'home.HomePage'
    ]

    
    content = StreamField(
        [
            ("partners", blocks.PartnerBlock()),     
        ],
        null=True,
        blank=True,
    )

    intro =  models.TextField(default='', blank=True, max_length=350)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('content'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        StreamFieldPanel("content"),
    ]

    keywords = models.CharField(default='', blank=True, max_length=150)

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(Page.promote_panels, heading=('Promote')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ]) 

    
class HomePage(Page):
    max_count=1
    template = "home/home-page.html"
    subpage_types = [
        'home.CustomPage',
        'home.PartnersSponsors',
        'home.Downloads',
        'home.Team',
        'home.Hardware',
        'home.Donations',
        'contact.ContactPage',
        'features',
        ]
    parent_page_types = [
        'wagtailcore.Page'
    ]

    content = StreamField(
        [
            ("richtext", blocks.RichtextBlock()),
            ("product_details", blocks.ProductBlock()),        
        ],
        null=True,
        blank=True,
    )

    manjaro_title = models.CharField(default='', blank=True, max_length=50)
    manjaro_intro = models.TextField(blank=True, max_length=350)
    promotion_text = models.CharField(default='', blank=True, max_length=80)
    promotion_url = models.URLField(blank=True)

    partners_title = models.CharField(default='', blank=True, max_length=50)
    partners_intro = models.TextField(blank=True, max_length=350)
    partners_url = models.URLField(blank=True)
    shells_title = models.CharField(default='', blank=True, max_length=50)
    shells_intro = models.TextField(blank=True, max_length=350)

    content_panels = Page.content_panels + [
        FieldPanel("manjaro_title"),
        FieldPanel("manjaro_intro"),
        FieldPanel("promotion_text"),
        FieldPanel("promotion_url"),
        FieldPanel("partners_title"),
        FieldPanel("partners_intro"),
        FieldPanel("partners_url"),
        FieldPanel("shells_title"),
        FieldPanel("shells_intro"),
        StreamFieldPanel("content"),
    ]

    keywords = models.CharField(default='', blank=True, max_length=100)

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=('Content')),
        ObjectList(Page.promote_panels, heading=('Promote')),
        ObjectList(Page.settings_panels, heading=('Settings')),
        YoastPanel(
            keywords='keywords',
            title='seo_title',
            search_description='search_description',
            slug='slug'
        ),
    ])
    