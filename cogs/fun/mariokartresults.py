import os
import sqlite3
from datetime import datetime
from discord.ext import commands

DATABASE_FOLDER = 'database'

class MarioKartResults(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.create_table()

    def create_table(self):
        db_path = os.path.join(DATABASE_FOLDER, 'mariokart_results.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                        player TEXT,
                        points INTEGER,
                        day TEXT)''')
        conn.commit()
        conn.close()

    @commands.slash_command(name='score')
    async def add_score(self, ctx, player: commands.MemberConverter, points: int):
        day = datetime.now().strftime('%Y-%m-%d')
        db_path = os.path.join(DATABASE_FOLDER, 'mariokart_results.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO results (player, points, day) VALUES (?, ?, ?)',
                       (str(player), points, day))
        conn.commit()
        conn.close()
        await ctx.send(f'Score added: {player} - {points} points on {day}')

    @commands.slash_command(name='leaderboard')
    async def leaderboard(self, ctx):
        db_path = os.path.join(DATABASE_FOLDER, 'mariokart_results.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT player, SUM(points) as total_points FROM results GROUP BY player ORDER BY total_points DESC')
        rows = cursor.fetchall()
        conn.close()
        if rows:
            leaderboard = '\n'.join([f'{row[0]}: {row[1]} points' for row in rows])
            await ctx.send(f'Leaderboard:\n{leaderboard}')
        else:
            await ctx.send('No leaderboard data found.')

def setup(bot):
    bot.add_cog(MarioKartResults(bot))
