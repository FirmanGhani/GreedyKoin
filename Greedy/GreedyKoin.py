import streamlit as st

def coin_change(X, arr):
    arr.sort(reverse=True)
    result = []
    count_dict = {coin: 0 for coin in arr}
    
    for coin in arr:
        while X >= coin:
            X -= coin
            result.append(coin)
            count_dict[coin] += 1
    
    if X != 0:
        st.write("Tidak bisa mendapatkan jumlah yang tepat dengan koin yang tersedia.")
    return result, count_dict

def main():
    st.title('Coin Change Problem')
    
    arr = [1, 2, 5, 10]
    st.write(f"Koin yang tersedia: {arr}")

    X = st.number_input("Masukkan nilai yang ingin dicari:", min_value=0, step=1)
    
    
    if st.button('Solve'):
        result, count_dict = coin_change(X, arr)
        
        if result:
            st.write(f"Kombinasi koin untuk mencapai {X} adalah: {result}")
            st.write("Jumlah setiap koin yang digunakan:")
            for coin, count in count_dict.items():
                if count > 0:
                    st.write(f"Koin {coin}: {count} kali")
    
if __name__ == "__main__":
    main()
