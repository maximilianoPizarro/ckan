# encoding: utf-8

import os
from setuptools import setup

# Avoid problem releasing to pypi from vagrant
if os.environ.get("USER", "") == "vagrant":
    del os.link

extras_require = {}
_extras_groups = [
    ("requirements", "requirements.txt"),
    ("dev", "dev-requirements.txt"),
]

HERE = os.path.dirname(__file__)
for group, filepath in _extras_groups:
    with open(os.path.join(HERE, filepath), "r") as f:
        extras_require[group] = f.readlines()

setup(
    message_extractors={
        "ckan": [
            ("**.py", "python", None),
            ("**.js", "javascript", None),
            ("templates/**.html", "ckan", None),
            ("templates/**.txt", "ckan", None),
            ("public/**", "ignore", None),
        ],
        "ckanext": [
            ("**.py", "python", None),
            ("**.js", "javascript", None),
            ("**.html", "ckan", None),
            ("multilingual/solr/*.txt", "ignore", None),
        ],
    },
    extras_require=extras_require,
    entry_points = {
    'paste.app_factory': [
        'main = ckan.config.middleware:make_app',
    ],
    'paste.app_install': [
        'main = ckan.config.install:CKANInstaller',
    ],
    'console_scripts': [
        'ckan = ckan.cli.cli:ckan',
    ],
    'ckan.click_command': [
        'datastore = ckanext.datastore.cli:datastore',
        'datapusher = ckanext.datapusher.cli:datapusher',
    ],
    'paste.paster_create_template': [
        'ckanext = ckan.pastertemplates:CkanextTemplate',
    ],
    'ckan.forms': [
        'standard = ckan.forms.package:get_standard_fieldset',
        'package = ckan.forms.package:get_standard_fieldset',
        'group = ckan.forms.group:get_group_fieldset',
        'package_group = ckan.forms.group:get_package_group_fieldset',
    ],
    'ckan.search': [
        'sql = ckan.lib.search.sql:SqlSearchBackend',
        'solr = ckan.lib.search.solr_backend:SolrSearchBackend',
    ],
        
    'ckan.plugins': [
        'stats = ckanext.stats.plugin:StatsPlugin',
        'multilingual_dataset = ckanext.multilingual.plugin:MultilingualDataset',
        'multilingual_group = ckanext.multilingual.plugin:MultilingualGroup',
        'multilingual_tag = ckanext.multilingual.plugin:MultilingualTag',
        'multilingual_resource = ckanext.multilingual.plugin:MultilingualResource',
        'expire_api_token = ckanext.expire_api_token.plugin:ExpireApiTokenPlugin',
        'chained_functions = ckanext.chained_functions.plugin:ChainedFunctionsPlugin',
        'datastore = ckanext.datastore.plugin:DatastorePlugin',
        'datapusher=ckanext.datapusher.plugin:DatapusherPlugin',
        'test_tag_vocab_plugin = ckanext.test_tag_vocab_plugin:MockVocabTagsPlugin',
        'resource_proxy = ckanext.resourceproxy.plugin:ResourceProxy',
        'text_view = ckanext.textview.plugin:TextView',
        'recline_view = ckanext.reclineview.plugin:ReclineView',
        'recline_grid_view = ckanext.reclineview.plugin:ReclineGridView',
        'recline_graph_view = ckanext.reclineview.plugin:ReclineGraphView',
        'recline_map_view = ckanext.reclineview.plugin:ReclineMapView',
        'datatables_view = ckanext.datatablesview.plugin:DataTablesView',
        'image_view = ckanext.imageview.plugin:ImageView',
        'audio_view = ckanext.audioview.plugin:AudioView',
        'video_view = ckanext.videoview.plugin:VideoView',
        'webpage_view = ckanext.webpageview.plugin:WebPageView',
        'hierarchy_display=ckanext.hierarchy.plugin:HierarchyDisplay',
        'hierarchy_form=ckanext.hierarchy.plugin:HierarchyForm',
        'hierarchy_group_form=ckanext.hierarchy.plugin:HierarchyGroupForm',
        #OAuth2
        'oauth2=ckanext.oauth2.plugin:OAuth2Plugin',

        'text_preview = ckanext.textview.plugin:TextView',
        'recline_preview = ckanext.reclineview.plugin:ReclineView',
        'recline_grid = ckanext.reclineview.plugin:ReclineGridView',
        'recline_graph = ckanext.reclineview.plugin:ReclineGraphView',
        'recline_map = ckanext.reclineview.plugin:ReclineMapView',
        # End of deprecated previews
        'example_itemplatehelpers = ckanext.example_itemplatehelpers.plugin:ExampleITemplateHelpersPlugin',
        'example_idatasetform = ckanext.example_idatasetform.plugin:ExampleIDatasetFormPlugin',
        'example_idatasetform_v1 = ckanext.example_idatasetform.plugin_v1:ExampleIDatasetFormPlugin',
        'example_idatasetform_v2 = ckanext.example_idatasetform.plugin_v2:ExampleIDatasetFormPlugin',
        'example_idatasetform_v3 = ckanext.example_idatasetform.plugin_v3:ExampleIDatasetFormPlugin',
        'example_idatasetform_v4 = ckanext.example_idatasetform.plugin_v4:ExampleIDatasetFormPlugin',
        'example_idatasetform_v5 = ckanext.example_idatasetform.plugin_v5:ExampleIDatasetFormPlugin',
        'example_idatasetform_v6 = ckanext.example_idatasetform.plugin_v6:ExampleIDatasetFormPlugin',
        'example_idatasetform_v7 = ckanext.example_idatasetform.plugin_v7:ExampleIDatasetFormPlugin',
        'example_igroupform = ckanext.example_igroupform.plugin:ExampleIGroupFormPlugin',
        'example_igroupform_v2 = ckanext.example_igroupform.plugin_v2:ExampleIGroupFormPlugin',
        'example_igroupform_default_group_type = ckanext.example_igroupform.plugin:ExampleIGroupFormPlugin_DefaultGroupType',
        'example_igroupform_organization = ckanext.example_igroupform.plugin:ExampleIGroupFormOrganizationPlugin',
        'example_iauthfunctions_v1 = ckanext.example_iauthfunctions.plugin_v1:ExampleIAuthFunctionsPlugin',
        'example_iauthfunctions_v2 = ckanext.example_iauthfunctions.plugin_v2:ExampleIAuthFunctionsPlugin',
        'example_iauthfunctions_v3 = ckanext.example_iauthfunctions.plugin_v3:ExampleIAuthFunctionsPlugin',
        'example_iauthfunctions_v4 = ckanext.example_iauthfunctions.plugin_v4:ExampleIAuthFunctionsPlugin',
        'example_iauthfunctions_v5_custom_config_setting = ckanext.example_iauthfunctions.plugin_v5_custom_config_setting:ExampleIAuthFunctionsPlugin',
        'example_iauthfunctions_v6_parent_auth_functions = ckanext.example_iauthfunctions.plugin_v6_parent_auth_functions:ExampleIAuthFunctionsPlugin',
        'example_theme_v01_empty_extension = ckanext.example_theme_docs.v01_empty_extension.plugin:ExampleThemePlugin',
        'example_theme_v02_empty_template = ckanext.example_theme_docs.v02_empty_template.plugin:ExampleThemePlugin',
        'example_theme_v03_jinja = ckanext.example_theme_docs.v03_jinja.plugin:ExampleThemePlugin',
        'example_theme_v04_ckan_extends = ckanext.example_theme_docs.v04_ckan_extends.plugin:ExampleThemePlugin',
        'example_theme_v05_block = ckanext.example_theme_docs.v05_block.plugin:ExampleThemePlugin',
        'example_theme_v06_super = ckanext.example_theme_docs.v06_super.plugin:ExampleThemePlugin',
        'example_theme_v07_helper_function = ckanext.example_theme_docs.v07_helper_function.plugin:ExampleThemePlugin',
        'example_theme_v08_custom_helper_function = ckanext.example_theme_docs.v08_custom_helper_function.plugin:ExampleThemePlugin',
        'example_theme_v09_snippet = ckanext.example_theme_docs.v09_snippet.plugin:ExampleThemePlugin',
        'example_theme_v10_custom_snippet = ckanext.example_theme_docs.v10_custom_snippet.plugin:ExampleThemePlugin',
        'example_theme_v11_HTML_and_CSS = ckanext.example_theme_docs.v11_HTML_and_CSS.plugin:ExampleThemePlugin',
        'example_theme_v12_extra_public_dir = ckanext.example_theme_docs.v12_extra_public_dir.plugin:ExampleThemePlugin',
        'example_theme_v13_custom_css = ckanext.example_theme_docs.v13_custom_css.plugin:ExampleThemePlugin',
        'example_theme_v14_more_custom_css = ckanext.example_theme_docs.v14_more_custom_css.plugin:ExampleThemePlugin',
        'example_theme_v15_fanstatic = ckanext.example_theme_docs.v15_fanstatic.plugin:ExampleThemePlugin',
        'example_theme_v16_initialize_a_javascript_module = ckanext.example_theme_docs.v16_initialize_a_javascript_module.plugin:ExampleThemePlugin',
        'example_theme_v17_popover = ckanext.example_theme_docs.v17_popover.plugin:ExampleThemePlugin',
        'example_theme_v18_snippet_api = ckanext.example_theme_docs.v18_snippet_api.plugin:ExampleThemePlugin',
        'example_theme_v19_01_error = ckanext.example_theme_docs.v19_01_error.plugin:ExampleThemePlugin',
        'example_theme_v19_02_error_handling = ckanext.example_theme_docs.v19_02_error_handling.plugin:ExampleThemePlugin',
        'example_theme_v20_pubsub = ckanext.example_theme_docs.v20_pubsub.plugin:ExampleThemePlugin',
        'example_theme_v21_custom_jquery_plugin = ckanext.example_theme_docs.v21_custom_jquery_plugin.plugin:ExampleThemePlugin',
        'example_theme_v22_fanstatic_and_webassets = ckanext.example_theme_docs.v22_fanstatic_and_webassets.plugin:ExampleThemePlugin',
        'example_theme_custom_config_setting = ckanext.example_theme_docs.custom_config_setting.plugin:ExampleThemePlugin',
        'example_theme_custom_emails = ckanext.example_theme_docs.custom_emails.plugin:ExampleCustomEmailsPlugin',
        'example_iresourcecontroller = ckanext.example_iresourcecontroller.plugin:ExampleIResourceControllerPlugin',
        'example_ivalidators = ckanext.example_ivalidators.plugin:ExampleIValidatorsPlugin',
        'example_iconfigurer = ckanext.example_iconfigurer.plugin:ExampleIConfigurerPlugin',
        'example_itranslation = ckanext.example_itranslation.plugin:ExampleITranslationPlugin',
        'example_iconfigurer_v1 = ckanext.example_iconfigurer.plugin_v1:ExampleIConfigurerPlugin',
        'example_iconfigurer_v2 = ckanext.example_iconfigurer.plugin_v2:ExampleIConfigurerPlugin',
        'example_flask_iblueprint = ckanext.example_flask_iblueprint.plugin:ExampleFlaskIBlueprintPlugin',
        'example_flask_streaming = ckanext.example_flask_streaming.plugin:ExampleFlaskStreamingPlugin',
        'example_iuploader = ckanext.example_iuploader.plugin:ExampleIUploader',
        'example_idatastorebackend = ckanext.example_idatastorebackend.plugin:ExampleIDatastoreBackendPlugin',
        'example_ipermissionlabels = ckanext.example_ipermissionlabels.plugin:ExampleIPermissionLabelsPlugin',
        'example_iapitoken = ckanext.example_iapitoken.plugin:ExampleIApiTokenPlugin',
        'example_iclick = ckanext.example_iclick.plugin:ExampleIClickPlugin',
        'example_iauthenticator = ckanext.example_iauthenticator.plugin:ExampleIAuthenticatorPlugin',
        'example_database_migrations = ckanext.example_database_migrations.plugin:ExampleDatabaseMigrationsPlugin',
    ],
    'ckan.system_plugins': [
        'synchronous_search = ckan.lib.search:SynchronousSearchPlugin',
        'domain_object_mods = ckan.model.modification:DomainObjectModificationExtension',
    ],
    'ckan.test_plugins': [
        'routes_plugin = tests.legacy.ckantestplugins:RoutesPlugin',
        'mapper_plugin = tests.legacy.ckantestplugins:MapperPlugin',
        'session_plugin = tests.legacy.ckantestplugins:SessionPlugin',
        'mapper_plugin2 = tests.legacy.ckantestplugins:MapperPlugin2',
        'authorizer_plugin = tests.legacy.ckantestplugins:AuthorizerPlugin',
        'test_observer_plugin = tests.legacy.ckantestplugins:PluginObserverPlugin',
        'action_plugin = tests.legacy.ckantestplugins:ActionPlugin',
        'auth_plugin = tests.legacy.ckantestplugins:AuthPlugin',
        'test_group_plugin = tests.legacy.ckantestplugins:MockGroupControllerPlugin',
        'test_package_controller_plugin = tests.legacy.ckantestplugins:MockPackageControllerPlugin',
        'test_resource_preview = tests.legacy.ckantestplugins:MockResourcePreviewExtension',
        'test_json_resource_preview = tests.legacy.ckantestplugins:JsonMockResourcePreviewExtension',
        'sample_datastore_plugin = ckanext.datastore.tests.sample_datastore_plugin:SampleDataStorePlugin',
        'example_datastore_deleted_with_count_plugin = ckanext.datastore.tests.test_chained_action:ExampleDataStoreDeletedWithCountPlugin',
        'example_data_store_search_sql_plugin = ckanext.datastore.tests.test_chained_auth_functions:ExampleDataStoreSearchSQLPlugin',
        'example_external_provider_plugin = ckanext.datastore.tests.test_chained_auth_functions:ExampleExternalProviderPlugin',
        'test_datastore_view = ckan.tests.lib.test_datapreview:MockDatastoreBasedResourceView',
        'test_datapusher_plugin = ckanext.datapusher.tests.test_interfaces:FakeDataPusherPlugin',
        'test_routing_plugin = ckan.tests.config.test_middleware:MockRoutingPlugin',
        'test_flash_plugin = ckan.tests.config.test_sessions:FlashMessagePlugin',
        'test_helpers_plugin = ckan.tests.lib.test_helpers:TestHelpersPlugin',
        'test_feed_plugin = ckan.tests.controllers.test_feed:MockFeedPlugin',
        'test_js_translations_plugin = ckan.tests.lib.test_i18n:TestJSTranslationsPlugin',
        'legacy_mock_search_plugin = ckan.tests.legacy.logic.test_action:MockPackageSearchPlugin',
    ],
    'babel.extractors': [
        'ckan = ckan.lib.extract:extract_ckan',
    ],


    }
)
