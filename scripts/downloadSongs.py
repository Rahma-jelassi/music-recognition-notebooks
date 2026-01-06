"""
Script: Télécharger 1000 chansons INDIVIDUELLES pour reconnaissance musicale
"""

import yt_dlp
import os
import time
import random
from pathlib import Path

# Configuration LOCALE
OUTPUT_DIR = r"C:\Users\Rahmaa\Desktop\deep learning\downloadSongs\audio_dataset_1000"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Recherches SPÉCIFIQUES - 10 chansons par artiste (plus de diversité!)
SEARCH_QUERIES = [
    # Pop anglais - Femmes
    "Dua Lipa songs", "Ariana Grande songs", "Taylor Swift songs",
    "Selena Gomez songs", "Katy Perry songs", "Adele songs",
    "Billie Eilish songs", "Olivia Rodrigo songs", "Doja Cat songs",
    "Avril Lavigne songs", "Shakira songs", "Rihanna songs",
    "Beyoncé songs", "Lady Gaga songs", "Miley Cyrus songs",
    
    # Pop anglais - Hommes
    "Ed Sheeran songs", "The Weeknd songs", "Harry Styles songs",
    "Justin Bieber songs", "Shawn Mendes songs", "Charlie Puth songs",
    "Bruno Mars songs", "Sam Smith songs", "Lewis Capaldi songs",
    
    # Rap/Hip-Hop
    "Drake songs", "Post Malone songs", "Travis Scott songs",
    "Kendrick Lamar songs", "J Cole songs", "Eminem songs",
    "Nicki Minaj songs", "Cardi B songs", "Megan Thee Stallion songs",
    
    # Rock/Alternative
    "Imagine Dragons songs", "Coldplay songs", "OneRepublic songs",
    "Twenty One Pilots songs", "Arctic Monkeys songs", "The Weeknd songs",
    
    # EDM/Electronic
    "Calvin Harris songs", "The Chainsmokers songs", "Marshmello songs",
    "David Guetta songs", "Avicii songs", "Martin Garrix songs",
    
    # Arabe - Femmes
    "Elissa songs", "إليسا أغاني", "Sherine songs", "شيرين عبد الوهاب",
    "Nancy Ajram songs", "نانسي عجرم", "Haifa Wehbe songs", "هيفاء وهبي",
    "Assala songs", "أصالة نصري", "Angham songs", "أنغام",
    "Ahlam songs", "أحلام", "Nawal El Zoghbi songs",
    
    # Arabe - Hommes
    "Amr Diab songs", "عمرو دياب أغاني", "Tamer Hosny songs", "تامر حسني",
    "Mohamed Ramadan songs", "محمد رمضان", "Saad Lamjarred songs",
    "Marwan Khoury songs", "مروان خوري", "Kadim Al Sahir songs",
    "Hussain Al Jassmi songs", "Ramy Sabry songs",
    
    # K-Pop - Groupes
    "BTS songs", "BLACKPINK songs", "TWICE songs", "Stray Kids songs",
    "NewJeans songs", "IVE songs", "Seventeen songs", "TXT songs",
    "Aespa songs", "ITZY songs", "Red Velvet songs",
    
    # Français
    "Indila songs", "Stromae songs", "Angèle songs", "Aya Nakamura songs",
    "Gims songs", "Maître Gims songs", "Dadju songs", "Nekfeu songs",
    "PNL songs", "Ninho songs", "Jul songs",
    
    # Espagnol/Latin
    "Bad Bunny songs", "Rosalía songs", "Karol G songs", "Shakira songs",
    "J Balvin songs", "Ozuna songs", "Maluma songs", "Daddy Yankee songs",
    "Tini songs", "TINI Stoessel songs", "Aitana songs",
    
    # Bollywood/Hindi
    "Arijit Singh songs", "Shreya Ghoshal songs", "Atif Aslam songs",
    "Neha Kakkar songs", "Armaan Malik songs",
    
    # Autres genres
    "Daft Punk songs", "The Chainsmokers songs", "Khalid songs",
    "SZA songs", "H.E.R. songs", "Lizzo songs",
    
    # Hits génériques (pour compléter)
    "viral songs 2024", "top hits 2024", "trending music 2024"
]

def download_individual_songs(query, max_songs=50):
    """
    Télécharge des chansons INDIVIDUELLES (pas de playlists/compilations)
    FILTRE: Seulement les vidéos de 2-6 minutes (vraies chansons)
    """
    
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'outtmpl': f'{OUTPUT_DIR}/%(artist)s - %(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'ignoreerrors': True,
        'extract_flat': False,
        'postprocessors': [],
        'match_filter': yt_dlp.utils.match_filter_func(
            "duration >= 120 & duration <= 360"
        ),
    }
    
    downloaded_count = 0
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_query = f"ytsearch{max_songs * 3}:{query} official audio"
            print(f"\n🔍 Recherche: {query}")
            
            info = ydl.extract_info(search_query, download=False)
            
            if info and 'entries' in info:
                entries = info['entries']
                
                for video in entries[:max_songs]:
                    if video is None:
                        continue
                    
                    duration = video.get('duration', 0)
                    title = video.get('title', 'Unknown')
                    
                    if 120 <= duration <= 360:
                        try:
                            print(f"   📥 {title} ({duration//60}:{duration%60:02d})")
                            ydl.download([video['webpage_url']])
                            downloaded_count += 1
                        except:
                            continue
                    else:
                        print(f"   ⏭️ Ignoré: {title} ({duration//60}:{duration%60:02d}) - Trop long/court")
                    
                    if downloaded_count >= max_songs:
                        break
            
            return True
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def count_downloaded_files():
    """Compte les fichiers audio téléchargés"""
    extensions = ['*.m4a', '*.webm', '*.mp3', '*.opus', '*.ogg']
    total = 0
    for ext in extensions:
        total += len(list(Path(OUTPUT_DIR).glob(ext)))
    return total

def get_unique_songs():
    """Retourne la liste des chansons uniques (évite doublons)"""
    audio_files = []
    extensions = ['.m4a', '.webm', '.mp3', '.opus', '.ogg']
    
    for file in Path(OUTPUT_DIR).iterdir():
        if file.suffix.lower() in extensions:
            audio_files.append(file.name)
    
    return sorted(set(audio_files))

def main():
    print("="*70)
    print("🎵 TÉLÉCHARGEMENT DE 1000 CHANSONS INDIVIDUELLES")
    print("="*70)
    print(f"📁 Dossier: {OUTPUT_DIR}")
    print(f"🎯 Objectif: 1000 fichiers audio séparés")
    print(f"💡 Utilisation: Reconnaissance musicale (Shazam-like avec YAMNet)\n")
    
    target = 1000
    downloaded = count_downloaded_files()
    
    print(f"📊 Fichiers déjà présents: {downloaded}\n")
    
    if downloaded >= target:
        print("✅ Objectif déjà atteint!")
        songs = get_unique_songs()
        print(f"\n📋 Exemples de chansons:")
        for song in songs[:10]:
            print(f"   • {song}")
        return
    
    # Mélanger les recherches pour diversifier
    random.shuffle(SEARCH_QUERIES)
    
    # Liste pour sauvegarder les recherches échouées
    failed_queries = []
    
    print("🔍 TÉLÉCHARGEMENT PAR RECHERCHES - PREMIER PASSAGE")
    print("-" * 70)
    
    for idx, query in enumerate(SEARCH_QUERIES):
        current_count = count_downloaded_files()
        
        if current_count >= target:
            print(f"\n🎉 Objectif atteint: {current_count} chansons!")
            break
        
        remaining = target - current_count
        songs_to_download = min(remaining, 10) 
        
        print(f"\n[{current_count}/{target}] Recherche {idx+1}/{len(SEARCH_QUERIES)}")
        
        before_count = count_downloaded_files()
        success = download_individual_songs(query, max_songs=songs_to_download)
        after_count = count_downloaded_files()
        
        added = after_count - before_count
        
        if added == 0 and not success:
            failed_queries.append(query)
            print(f"   ⚠️ Recherche échouée - Sera réessayée plus tard")
        
        print(f"   ✅ +{added} nouvelles chansons (Total: {after_count})")
        
        if idx < len(SEARCH_QUERIES) - 1:
            wait_time = 5
            print(f"   ⏳ Pause de {wait_time}s...")
            time.sleep(wait_time)
    
    # RÉESSAYER LES RECHERCHES ÉCHOUÉES
    if failed_queries and count_downloaded_files() < target:
        print("\n" + "="*70)
        print(f"🔄 RÉESSAI DES {len(failed_queries)} RECHERCHES ÉCHOUÉES")
        print("="*70)
        
        for idx, query in enumerate(failed_queries):
            current_count = count_downloaded_files()
            
            if current_count >= target:
                print(f"\n🎉 Objectif atteint: {current_count} chansons!")
                break
            
            remaining = target - current_count
            songs_to_download = min(remaining, 10) 
            
            print(f"\n[{current_count}/{target}] Réessai {idx+1}/{len(failed_queries)}: {query}")
            
            before_count = count_downloaded_files()
            download_individual_songs(query, max_songs=songs_to_download)
            after_count = count_downloaded_files()
            
            added = after_count - before_count
            print(f"   ✅ +{added} nouvelles chansons (Total: {after_count})")
            
            if idx < len(failed_queries) - 1:
                wait_time = 10
                print(f"   ⏳ Pause de {wait_time}s...")
                time.sleep(wait_time)
    
    final_count = count_downloaded_files()
    
    print("\n" + "="*70)
    print("📊 RÉSUMÉ FINAL")
    print("="*70)
    print(f"✅ Chansons téléchargées: {final_count}")
    print(f"📁 Emplacement: {OUTPUT_DIR}")
    
    total_size = 0
    for file in Path(OUTPUT_DIR).iterdir():
        if file.is_file():
            total_size += file.stat().st_size
    
    total_size_gb = total_size / (1024**3)
    print(f"💾 Taille totale: {total_size_gb:.2f} GB")
    
    # Afficher quelques exemples
    songs = get_unique_songs()
    print(f"\n📋 Exemples de chansons ({min(10, len(songs))} sur {len(songs)}):")
    for song in songs[:10]:
        print(f"   • {song}")
    
    if final_count < target:
        print(f"\n⚠️ Objectif non atteint: {target - final_count} chansons manquantes")
        print("   💡 Relance le script pour continuer le téléchargement!")
    else:
        print(f"\n🎉 SUCCÈS! Dataset complet: {final_count} chansons individuelles")
        print("   ✅ Prêt pour:")
        print("      1. Prétraitement audio")
        print("      2. Extraction embeddings YAMNet")
        print("      3. Reconnaissance musicale en temps réel")

if __name__ == "__main__":
    main()