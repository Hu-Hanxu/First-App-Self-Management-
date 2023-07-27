import requests
import json

BASE_URL = 'http://172.25.3.19:5000/api'

def test_add_choice():
    # 選択肢を追加するAPIをテストする
    data = {
        'choices': ['Option 1', 'Option 2', 'Option 3', 'Option 4']
    }
    response = requests.post(f'{BASE_URL}/choices', json=data)
    assert response.status_code == 200
    result = response.json()
    assert 'message' in result and 'choice_id' in result
    print('選択肢を追加しました！')
    return result['choice_id']

def test_get_random_choice(choice_id):
    # ランダムな選択肢を取得するAPIをテストする
    response = requests.get(f'{BASE_URL}/choices/{choice_id}/random')
    assert response.status_code == 200
    result = response.json()
    assert 'random_choice' in result
    print('ランダムな選択肢:', result['random_choice'])

def test_delete_choice(choice_id):
    # 選択肢を削除するAPIをテストする
    response = requests.delete(f'{BASE_URL}/choices/{choice_id}')
    assert response.status_code == 200
    result = response.json()
    assert 'message' in result
    print('選択肢を削除しました！')

if __name__ == '__main__':
    try:
        # 選択肢を追加
        choice_id = test_add_choice()

        # ランダムな選択肢を取得
        test_get_random_choice(choice_id)

        # 選択肢を削除
        test_delete_choice(choice_id)
    except Exception as e:
        print('テスト中にエラーが発生しました:', e)
