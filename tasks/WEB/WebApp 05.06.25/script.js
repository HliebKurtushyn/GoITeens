const songs = [
    "Imagine Dragons - Believer",
    "Ed Sheeran - Shape of You",
    "Beyoncé - Halo",
    "The Weeknd - Blinding Lights",
    "Coldplay - Viva La Vida",
    "Adele - Rolling in the Deep",
    "Maroon 5 - Sugar",
    "OneRepublic - Counting Stars",
    "Taylor Swift - Shake It Off",
    "Post Malone - Circles",
    "Shawn Mendes - Treat You Better",
    "Justin Bieber - Love Yourself",
    "Dua Lipa - Don't Start Now",
    "Lady Gaga - Shallow",
    "Billie Eilish - Bad Guy",
    "Bruno Mars - Uptown Funk",
    "Harry Styles - Watermelon Sugar",
    "Chainsmokers - Closer",
    "Linkin Park - Numb",
    "Katy Perry - Roar",
    "Sam Smith - Stay With Me"
];

const button = document.getElementById("us_button");
const user_input = document.getElementById("user_value")
const result = document.getElementById("result");

button.addEventListener("click", () => {
    const song_index = songs.findIndex(song => song.includes(user_input.value))
    if (song_index === -1) {
      result.textContent = "Пісні не знайдено в збірці"
    } else {
    result.textContent = `Пісню ${songs[song_index]} знайдено в збірці на №${song_index + 1}`};

});