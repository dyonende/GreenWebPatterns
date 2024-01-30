import glob
import json
import os
import sys

print("name,performance_score,sustainability_score,unminified_html_score,unminified_html_value,unminified_css_score, unminified_css_value,unminified_js_score,unminified_js_value,video_codec_score,video_codec_value,font_family_score,font_family_value,font_format_score,font_format_value,responsive_images_score,responsive_images_value,optimised_images_score,optimised_images_value,text_compression_score,text_compression_value")

for path in glob.glob('/mnt/d/dev/GreenWebPatterns/UniAnalysis/data/top100results/raw/*.json'): 
    with open(path) as f:
        report = json.load(f)
        
    name = os.path.splitext(os.path.basename(path))[0].replace(',', '')
    if "runtimeError" in report:
        print(name, "has failed", file=sys.stderr)
    else:
        #category scores
        performance_score = report['categories']['performance']['score']
        sustainability_score = report['categories']['lighthouse-plugin-sus']['score']
        
        #audit scores
        unminified_html_score = report['audits']['unminified-html']['score']
        unminified_html_value = report['audits']['unminified-html']['numericValue']
        
        unminified_css_score = report['audits']['unminified-css']['score']
        try:
            unminified_css_value = report['audits']['unminified-css']['numericValue']
        except:
            unminified_css_value = None
        
        unminified_js_score = report['audits']['unminified-javascript']['score']
        try:
            unminified_js_value = report['audits']['unminified-javascript']['numericValue']
        except:
            unminified_js_value = None
        
        video_codec_score = report['audits']['video-codec']['score']
        try:
            video_codec_value = report['audits']['video-codec']['numericValue']
        except:
            video_codec_value = None
            
        font_family_score = report['audits']['font-family']['score']
        try:
            font_family_value = report['audits']['font-family']['numericValue']
        except:
            font_family_value = None
        
        font_format_score = report['audits']['font-format']['score']
        try:
            font_format_value = report['audits']['font-format']['numericValue']
        except:
            font_format_value = None
        
        responsive_images_score = report['audits']['uses-responsive-images']['score']
        try:
            responsive_images_value = report['audits']['uses-responsive-images']['numericValue']
        except:
            responsive_images_value = None
        
        optimised_images_score = report['audits']['uses-optimized-images']['score']
        try:
            optimised_images_value = report['audits']['uses-optimized-images']['numericValue']
        except:
            optimised_images_value = None
        
        text_compression_score = report['audits']['uses-text-compression']['score']
        try:
            text_compression_value = report['audits']['uses-text-compression']['numericValue']
        except:
            text_compression_value = None
        
        print(name, performance_score, sustainability_score, unminified_html_score, unminified_html_value, unminified_css_score, unminified_css_value, unminified_js_score, unminified_js_value, video_codec_score, video_codec_value, font_family_score, font_family_value, font_format_score, font_format_value, responsive_images_score, responsive_images_value, optimised_images_score, optimised_images_value, text_compression_score, text_compression_value, sep=',')
        
        