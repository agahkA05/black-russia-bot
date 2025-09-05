@echo off
echo 🚀 Быстрое обновление бота...

git add .
git commit -m "Auto update - %date% %time%"
git push origin main

echo ✅ Готово! Бот обновится через 1-2 минуты
timeout /t 3
