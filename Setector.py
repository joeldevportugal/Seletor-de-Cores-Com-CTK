from tkinter import messagebox
import customtkinter

def copiar_rgb():
    codigo = ERGB.get()
    if codigo:
        janela.clipboard_clear()
        janela.clipboard_append(codigo)
    else:
        messagebox.showwarning("Aviso", "Não há codico para copiar.")

def copiar_Hexa():
    codigo = EHexa.get()
    if codigo :
        janela.clipboard_clear()
        janela.clipboard_append(codigo)
    else:
        messagebox.showwarning("Aviso", "Não há codico para copiar.")

def atualizar_cor_vermelho(valor_slider):
    valor_vermelho = int(valor_slider)
    Lvermelho.configure(text=f'Vermelho: {valor_vermelho}')
    atualizar_cor()

def atualizar_cor_verde(valor_slider):
    valor_verde = int(valor_slider)
    Lverde.configure(text=f'Verde: {valor_verde}')
    atualizar_cor()

def atualizar_cor_azul(valor_slider):
    valor_azul = int(valor_slider)
    LAzul.configure(text=f'Azul: {valor_azul}')
    atualizar_cor()

def atualizar_cor():
    vermelho = int(Svermelho.get())  # Convertendo para inteiro
    verde = int(Sverde.get())  # Convertendo para inteiro
    azul = int(SAzul.get())  # Convertendo para inteiro
    cor_hexadecimal = f'#{vermelho:02x}{verde:02x}{azul:02x}'
    PCor.configure(bg=cor_hexadecimal)
    Lvermelho_valor.configure(text=str(vermelho))
    Lverde_valor.configure(text=str(verde))
    LAzul_valor.configure(text=str(azul))
    EHexa.delete(0, 'end')
    EHexa.insert('end', cor_hexadecimal)
    ERGB.delete(0, 'end')
    ERGB.insert('end', f'{vermelho}, {verde}, {azul}')

def limpar_campos():
    codigo_hex = EHexa.get()
    codigo_rgb = ERGB.get()

    if codigo_hex or codigo_rgb:
        # Define os valores padrão para os sliders e rótulos
        Svermelho.set(0)
        Sverde.set(0)
        SAzul.set(0)
        Lvermelho.configure(text='Vermelho:0')
        Lverde.configure(text='Verde:0')
        LAzul.configure(text='Azul:0')
        # Define a cor padrão para o painel
        PCor.configure(bg='Black')
        # Limpa as entradas e exibe o placeholder text
        EHexa.delete(0, 'end')
        EHexa.insert(0, 'Codico Hexadecimal')  # Define o placeholder text novamente
        ERGB.delete(0, 'end')
        ERGB.insert(0, 'Codico RGB')  # Define o placeholder text novamente
    else:
        messagebox.showwarning('Aviso','Nao a codicos a Limpar')
       
# Defenir as Cores a Usar -----------------------------------------
co0='#FFFFFF' # cor Fundo 
co1='#F4F1F2' # cor Botões
co2='#000000' # cor Letra Botões

#------------------------------------------------------------------
#Configurar a Nossa Janela-----------------------------------------
janela = customtkinter.CTk()
janela.geometry('900x280+100+100')
janela.resizable(False, False)
janela.title('Selector CTK Dev Joel PT 2024 ©')
janela.config(bg=co0)
janela.iconbitmap('C:\\Users\HP\\Desktop\\Python customtkinter\\Selector de Cores\\icon.ico')
#------------------------------------------------------------------
# criar O painel cor Posicionar e configurar a Cor de Fundo -------
PCor = customtkinter.CTkCanvas(janela) # criar O nosso Painel
PCor.configure(bg='Black') # defenir a Nossa Cor do Fundo
PCor.place(x=10, y=10) # posicionar O Painel
#------------------------------------------------------------------
# criar O label vermelho Posicionar O label e criar O slider vermelho e posicionar-------
Lvermelho = customtkinter.CTkLabel(janela, text='Vermelho:0', font=("Arial", 15, 'bold'), bg_color=co0)
Lvermelho.place(x=320, y=10)
Svermelho = customtkinter.CTkSlider(janela, from_=0, to=255, width=580, command=atualizar_cor_vermelho, bg_color=co0)
Svermelho.place(x=320, y=40)
# Label para exibir o valor de vermelho
Lvermelho_valor = customtkinter.CTkLabel(janela, text='0', font=("Arial", 12))
Lvermelho_valor.place(x=900, y=40)
#----------------------------------------------------------------------------------------
# criar O label Verde e o Slider Verde E posicionar Ambos -------------------------------
Lverde = customtkinter.CTkLabel(janela, text='Verde:0', font=("Arial", 15, 'bold'),bg_color=co0)
Lverde.place(x=320, y=80)
Sverde = customtkinter.CTkSlider(janela, from_=0, to=255, width=580, command=atualizar_cor_verde, bg_color=co0)
Sverde.place(x=320, y=110)
# Label para exibir o valor de verde
Lverde_valor = customtkinter.CTkLabel(janela, text='0', font=("Arial", 12))
Lverde_valor.place(x=900, y=110)
#----------------------------------------------------------------------------------------
# criar O label Azul e o Slider e Posicionar Ambos --------------------------------------
LAzul = customtkinter.CTkLabel(janela, text='Azul:0', font=("Arial", 15, 'bold'), bg_color=co0)
LAzul.place(x=320, y=150)
SAzul = customtkinter.CTkSlider(janela, from_=0, to=255, width=580, command=atualizar_cor_azul, bg_color=co0)
SAzul.place(x=320, y=180)
# Label para exibir o valor de azul
LAzul_valor = customtkinter.CTkLabel(janela, text='0', font=("Arial", 12))
LAzul_valor.place(x=900, y=180)
#-----------------------------------------------------------------------------------------
# criar a entry Ehexa e o Botão Copiar --------------------------------------------------
EHexa = customtkinter.CTkEntry(janela, placeholder_text='Codico Hexadecimal', bg_color=co0) 
EHexa.place(x=10, y=235)
CopiarHexa= customtkinter.CTkButton(janela, text='Copiar Hexadecimal', command=copiar_Hexa, font=("Arial", 12,'bold'), bg_color=co0, fg_color=co1, text_color=co2)
CopiarHexa.place(x=155, y=235)
#-----------------------------------------------------------------------------------------
# criar a entry ERGB e o Botão Copiar-----------------------------------------------------
ERGB = customtkinter.CTkEntry(janela, placeholder_text='Codico RGB', bg_color=co0) 
ERGB.place(x=300, y=235)
CopiarRGB= customtkinter.CTkButton(janela, text='Copiar RGB', command=copiar_rgb, font=("Arial", 12,'bold'),bg_color=co0, fg_color=co1, text_color=co2)
CopiarRGB.place(x=445, y=235) 
#-----------------------------------------------------------------------------------------
# criar O botão Limpar -------------------------------------------------------------------
Blimpar = customtkinter.CTkButton(janela, text='Limpar Codico', command=limpar_campos, font=("Arial", 12,'bold'), bg_color=co0,fg_color=co1, text_color=co2)
Blimpar.place(x=590, y=235) 
# iniciar a Nossa Janela -----------------------------------------------------------------
janela.mainloop()
#-----------------------------------------------------------------------------------------