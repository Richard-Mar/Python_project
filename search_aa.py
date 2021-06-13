aa_dict = {'W':"色氨酸 Trp",'K':'赖氨酸 Lys','A':'丙氨酸 Ala','R':'精氨酸 Arg',
           'N':'天冬酰胺 Asn','D':'天冬氨酸 Asp','C':'半胱氨酸 Cys','Q':'谷氨酰胺 Gln',
           'E':'谷氨酸 Glu','H':'组氨酸 His','I':'异亮氨酸 Ile','L':'亮氨酸 Leu',
           'M':'甲硫氨酸/蛋氨酸 Met','F':'苯丙氨酸 Phe','P':'脯氨酸 Pro','S':'丝氨酸',
           'T':'苏氨酸 Thr','Y':'酪氨酸 Tyr','V':'缬氨酸 Val','G':'甘氨酸 Gla'}

def search_aa(letter):
    try:
        aa,aa_symbol = aa_dict[letter].split()
        print(f"输入查询：{letter}\n该氨基酸中文名为 {aa} ,英文三字母为 {aa_symbol} ")
    except:
        print("20种氨基酸中不存在该简写!")

if __name__ == '__main__':
    letter = input("请输入要查询氨基酸的英文子母简写:")
    search_aa(letter)