import streamlit as st

st.set_page_config(page_title="Prompt Generator Video", layout="wide")

st.title("🎬 Generator Prompt Video - By Dothey")
st.markdown("Isi detail berikut untuk menciptakan prompt video yang kaya dan spesifik.")

with st.form("prompt_form"):
    col1, col2 = st.columns(2)

    with col1:
        subjek = st.text_input("1. Subjek Utama", "seorang astronot tua, seekor rubah oranye")
        aksi = st.text_input("2. Aksi/Kegiatan Subjek", "memperbaiki satelit, melayang di udara")
        lokasi = st.text_input("3. Latar/Lokasi", "di orbit bumi, di dalam hutan berkabut")
        pencahayaan = st.text_input("4. Waktu & Pencahayaan", "golden hour, malam hari neon")

    with col2:
        gaya = st.text_input("5. Gaya Visual & Estetika", "sinematik 8K, Ghibli style")
        kamera = st.text_input("6. Pengambilan Gambar (Kamera)", "drone shot, close-up")
        mood = st.text_input("7. Suasana (Mood) & Emosi", "misterius, ceria, melankolis")
        detail = st.text_input("8. Detail Spesifik Tambahan", "pantulan cahaya, uap kopi")

    dialog = st.text_area("9. Dialog dalam Adegan (opsional)", 
        'ELARA: "Apakah kau lihat bintang jatuh itu?"\nKAI: "Itu bukan bintang... itu kapal."')

    negatif = st.text_input("10. Hal yang Dihindari (Prompt Negatif)", 
                            "kualitas rendah, buram, watermark, wajah aneh")

    submitted = st.form_submit_button("🎨 Buat Prompt")

if submitted:
    # Prompt Inti
    prompt_inti = f"{subjek} {aksi} di {lokasi}."

    # Prompt Detail
    kalimat_deskriptif = [
        prompt_inti,
        f"Gaya visualnya {gaya} dengan pencahayaan {pencahayaan}.",
        f"Pengambilan gambar menggunakan {kamera}, menciptakan suasana yang {mood}.",
    ]
    if detail:
        kalimat_deskriptif.append(f"Detail penting termasuk {detail}.")
    prompt_detail = " ".join(kalimat_deskriptif)

    # Prompt Final
    final_parts = [
        f"{subjek} {aksi} di {lokasi}.",
        f"Gaya visual: {gaya}, {pencahayaan}, suasana {mood}.",
        f"Shot kamera: {kamera}.",
    ]
    if detail:
        final_parts.append(f"Detail tambahan: {detail}.")
    if dialog:
        final_parts.append(f"Deskripsi adegan dengan dialog: {dialog.replace(chr(10), ' ')}")
    if negatif:
        final_parts.append(f"--no {negatif}")

    prompt_final = " ".join(final_parts)

    # Output
    st.success("✅ Prompt Anda Telah Siap!")

    st.subheader("1. Versi Ringkas (Untuk ide cepat)")
    st.code(prompt_inti)

    st.subheader("2. Versi Deskriptif (Penjelasan lengkap)")
    st.write(prompt_detail)
    if dialog:
        st.markdown("**Dialog dalam adegan:**")
        st.text(dialog)

    st.subheader("3. PROMPT FINAL (Siap Copy-Paste ke VEO)")
    st.text_area("Prompt Final", value=prompt_final, height=200)

    st.download_button("⬇️ Download Prompt", prompt_final, file_name="veo_prompt.txt")

