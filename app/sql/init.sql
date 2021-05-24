CREATE TABLE captcha_discord(
    id INTEGER PRIMARY KEY,
    verification_captcha VARCHAR(10),
    id_user VARCHAR(18) UNIQUE
)