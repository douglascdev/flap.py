# class Controlador:
#     def __init__(self, **settings):
#         self.__dict__.update(settings)
#         jogo
#         self.done = False
#         self.screen = pg.display.set_mode(self.size)
#         self.clock = pg.time.Clock()
#
#     def setup_states(self, state_dict, start_state):
#         self.state_dict = state_dict
#         self.state_name = start_state
#         self.state = self.state_dict[self.state_name]
#
#     def flip_state(self):
#         self.state.finalizada = False
#         previous, self.state_name = self.state_name, self.state.proxima
#         self.state.limpar()
#         self.state = self.state_dict[self.state_name]
#         self.state.iniciar()
#         self.state.anterior = previous
#
#     def update(self, dt):
#         if self.state.sair:
#             self.done = True
#         elif self.state.finalizada:
#             self.flip_state()
#         self.state.update(self.screen, dt)
#
#     def event_loop(self):
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 self.done = True
#             self.state.get_evento(event)
#
#     def main_game_loop(self):
#         while not self.done:
#             delta_time = self.clock.tick(self.fps) / 1000.0
#             self.event_loop()
#             self.atualizar(delta_time)
#             pg.display.update()
