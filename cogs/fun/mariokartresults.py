import os
import sqlite3
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
                        day TEXT,
                        entry_by TEXT)''')
        conn.commit()
        conn.close()

    @commands.slash_command(name='score')
    async def add_score(self, ctx, player: str, points: int, day: str, entry_by: str):
        db_path = os.path.join(DATABASE_FOLDER, 'mariokart_results.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO results (player, points, day, entry_by) VALUES (?, ?, ?, ?)',
                       (player, points, day, entry_by))
        conn.commit()
        conn.close()
        await ctx.send(f'Score added: {player} - {points} points on {day} by {entry_by}')

    @commands.slash_command(name='get_scores')
    async def get_scores(self, ctx):
        db_path = os.path.join(DATABASE_FOLDER, 'mariokart_results.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM results')
        rows = cursor.fetchall()
        conn.close()
        if rows:
            results = '\n'.join([f'{row[0]}: {row[1]} points on {row[2]} by {row[3]}' for row in rows])
            await ctx.send(f'Race Results:\n{results}')
        else:
            await ctx.send('No results found.')

def setup(bot):
    bot.add_cog(MarioKartResults(bot))
