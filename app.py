from flask import Flask, render_template, request, redirect, url_for, flash
import yt_dlp
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('main.html', year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        flash('يرجى إدخال رابط الفيديو', 'danger')
        return redirect(url_for('index'))
    try:
        # yt-dlp يدعم يوتيوب، تويتر، تيك توك، انستقرام
        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'quiet': True,
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info['url']
            title = info.get('title', 'فيديو')
            thumbnail = info.get('thumbnail', '')
            duration = info.get('duration', 0)
            platform = ''
            if 'youtube.com' in url or 'youtu.be' in url:
                platform = 'YouTube'
            elif 'twitter.com' in url:
                platform = 'Twitter'
            elif 'tiktok.com' in url:
                platform = 'TikTok'
            elif 'instagram.com' in url:
                platform = 'Instagram'
            else:
                platform = 'منصة غير معروفة'
            return render_template('preview.html', video_url=video_url, title=title, thumbnail=thumbnail, duration=duration, platform=platform, year=datetime.now().year)
    except Exception as e:
        flash(f'حدث خطأ أثناء التحميل: {str(e)}', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
