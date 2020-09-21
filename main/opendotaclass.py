import requests


class OpenDota:
    #TODO
    # 1. Необходимо добавить вызов методов:
    # --- 1. records     - https://docs.opendota.com/#tag/records
    # --- 2. scenarios   - https://docs.opendota.com/#tag/scenarios
    # 2. Проверить вызов методов:
    # --- 1. heroes()
    # --- 2. matches()
    # --- 3. job_request() - также дописать описание метода

    token = None
    base_url = 'https://api.opendota.com/api/'
    params = {
        'api_key': token
    }
    def __init__(self, token=None):
        if token is not None:
            self.token = token

    def api_auth_check(self, params):
        """ Функция проверки, вызывается ли метод с ключом. Если с ключом, то добавляет его в параметры вызова методоа
        """
        if self.token is not None:
            params += self.params
        return params

    def uni_request(self, req_name, params=None, req_type='get'):
        """ Функция выполнения запросов с параметрами, но спростым url (т.е. без переменных)
        Параметры:
        --- req_name: Наименование метода API Opendota (Список доступных методов указан ниже)
        --- params: Словарь параметров вызываемого метода
        --- req_type: Тип запроса вызываемого метода
        Список доступных методов:
            1.  playersByRank   (https://docs.opendota.com/#tag/playersByRank%2Fpaths%2F~1playersByRank%2Fget)
            2.  proPlayers      (https://docs.opendota.com/#tag/pro-players%2Fpaths%2F~1proPlayers%2Fget)
            3.  proMatches      (https://docs.opendota.com/#tag/pro-matches%2Fpaths%2F~1proMatches%2Fget)
            4.  publicMatches   (https://docs.opendota.com/#tag/public-matches%2Fpaths%2F~1publicMatches%2Fget)
            5.  parsedMatches   (https://docs.opendota.com/#tag/parsed-matches%2Fpaths%2F~1parsedMatches%2Fget)
            6.  metadata        (https://docs.opendota.com/#tag/metadata%2Fpaths%2F~1metadata%2Fget)
            7.  distributions   (https://docs.opendota.com/#tag/distributions%2Fpaths%2F~1distributions%2Fget)
            8.  search          (https://docs.opendota.com/#tag/search%2Fpaths%2F~1search%2Fget)
            9.  rankings        (https://docs.opendota.com/#tag/rankings%2Fpaths%2F~1rankings%2Fget)
            10. benchmarks      (https://docs.opendota.com/#tag/benchmarks%2Fpaths%2F~1benchmarks%2Fget)
            11. status          (https://docs.opendota.com/#tag/status%2Fpaths%2F~1status%2Fget)
            12. health          (https://docs.opendota.com/#tag/health%2Fpaths%2F~1health%2Fget)
            13. FindMatches     (https://docs.opendota.com/#tag/findMatches%2Fpaths%2F~1findMatches%2Fget)
            14. heroStats       (https://docs.opendota.com/#tag/hero-stats%2Fpaths%2F~1heroStats%2Fget)
            15. leagues         (https://docs.opendota.com/#tag/leagues%2Fpaths%2F~1leagues%2Fget)
            16. replays         (https://docs.opendota.com/#tag/replays%2Fpaths%2F~1replays%2Fget)
            17. live            (https://docs.opendota.com/#tag/live%2Fpaths%2F~1live%2Fget)
            18. schema          (https://docs.opendota.com/#tag/schema%2Fpaths%2F~1schema%2Fget)
        """
        req_list_allowed = ['playersByRank', 'proPlayers', 'proMatches', 'publicMatches', 'parsedMatches',
                            'explorer', 'metadata', 'distributions', 'search', 'rankings', 'benchmarks',
                            'status', 'health', 'FindMatches', 'heroStats', 'leagues', 'replays',
                            'live', 'schema', 'constants']
        if req_name not in req_list_allowed:
            return 'Вызываемый метод не из списка: {}'.format(req_list_allowed)
        params = self.api_auth_check(params)
        url = '{}{}'.format(self.base_url, req_name)
        if req_type == 'get':
            response = requests.get(url, params=params)
        elif req_type == 'post':
            response = requests.post(url, params=params)
        else:
            return 'Можно выполнять только GET и POST запросы'
        result = response.json()
        return result

    def teams(self, team_id=None, req_name=None):
        """ Функция для вызова методов API Opendota, относящихся к командам Dota 2
        Параметры:
        --- team_id: ID команды. Можно найти в клиенте Dota 2
        --- req_name: Наименование метода API Opendota (Список доступных методов указан ниже)
        Список доступных методов:
            1.  teams                   (https://docs.opendota.com/#tag/teams%2Fpaths%2F~1teams%2Fget)
            2.  teams/{team_id}         (https://docs.opendota.com/#tag/teams%2Fpaths%2F~1teams~1%7Bteam_id%7D%2Fget)
            3.  teams/{team_id}/matches (https://docs.opendota.com/#tag/teams%2Fpaths%2F~1teams~1%7Bteam_id%7D~1matches%2Fget)
            4.  teams/{team_id}/players (https://docs.opendota.com/#tag/teams%2Fpaths%2F~1teams~1%7Bteam_id%7D~1players%2Fget)
            5.  teams/{team_id}/heroes  (https://docs.opendota.com/#tag/teams%2Fpaths%2F~1teams~1%7Bteam_id%7D~1heroes%2Fget)
        """
        req_list_allowed = ['matches', 'players', 'heroes']
        params = {
            'team_id': team_id
        }
        params = self.api_auth_check(params)

        if not team_id:
            req_name = None
            url = '{}{}'.format(self.base_url, 'teams')
            response = requests.get(url)
        else:
            if req_name == None:
                url = '{}teams/{}'.format(self.base_url, team_id)
                response = requests.get(url, params=params)
            elif req_name not in req_list_allowed:
                return 'Вызываемый метод не из списка: {}'.format(req_list_allowed)
            else:
                url = '{}teams/{}/{}'.format(self.base_url, team_id, req_name)
                response = requests.get(url, params=params)
        result = response.json()
        return result

    def players(self, account_id, req_name=None):
        """ Функция для вызова методов API Opendota, относящихся к игрокам Dota 2
        Параметры:
        --- account_id: Steam32 ID игрока.
        --- req_name: Наименование метода API Opendota (Список доступных методов указан ниже)
        Список доступных методов:
            1.  players/{account_id}                (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D%2Fget)
            2.  players/{account_id}/wl             (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1wl%2Fget)
            3.  players/{account_id}/recentMatches  (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1recentMatches%2Fget)
            4.  players/{account_id}/matches        (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1matches%2Fget)
            5.  players/{account_id}/heroes         (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1heroes%2Fget)
            6.  players/{account_id}/peers          (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1peers%2Fget)
            7.  players/{account_id}/pros           (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1pros%2Fget)
            8.  players/{account_id}/totals         (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1totals%2Fget)
            9.  players/{account_id}/counts         (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1counts%2Fget)
            10. players/{account_id}/histograms     (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1histograms~1%7Bfield%7D%2Fget)
            11. players/{account_id}/wardmap        (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1wardmap%2Fget)
            12. players/{account_id}/wordcloud      (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1wordcloud%2Fget)
            13. players/{account_id}/ratings        (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1ratings%2Fget)
            14. players/{account_id}/rankings       (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1rankings%2Fget)
            15. players/{account_id}/refresh        (https://docs.opendota.com/#tag/players%2Fpaths%2F~1players~1%7Baccount_id%7D~1refresh%2Fpost)
        """
        req_list_allowed = ['wl', 'recentMatches', 'matches', 'heroes', 'peers',
                            'pros', 'totals', 'counts', 'histograms', 'wardmap', 'wordcloud',
                            'ratings', 'rankings', 'refresh']
        params = {
            'account_id': account_id
        }
        params = self.api_auth_check(params)

        if req_name == None:
            url = '{}players/{}'.format(self.base_url, account_id)
            response = requests.get(url, params=params)
        elif req_name not in req_list_allowed:
            return 'Вызываемый метод не из списка: {}'.format(req_list_allowed)
        else:
            url = '{}players/{}/{}'.format(self.base_url, account_id, req_name)
            response = requests.get(url, params=params)
        result = response.json()
        return result

    def heroes(self, hero_id=None, req_name=None):
        """ Функция для вызова методов API Opendota, относящихся к героям Dota 2
        Параметры:
        --- hero_id: ID команды. Можно найти в клиенте Dota 2
        --- req_name: Наименование метода API Opendota (Список доступных методов указан ниже)
        Список доступных методов:
            1.  heroes                          (https://docs.opendota.com/#tag/heroes%2Fpaths%2F~1heroes%2Fget)
            2.  heroes/{hero_id}/matches        (https://docs.opendota.com/#tag/heroes%2Fpaths%2F~1heroes~1%7Bhero_id%7D~1matches%2Fget)
            3.  heroes/{hero_id}/matchups       (https://docs.opendota.com/#tag/heroes%2Fpaths%2F~1heroes~1%7Bhero_id%7D~1matchups%2Fget)
            4.  heroes/{hero_id}/durations      (https://docs.opendota.com/#tag/heroes%2Fpaths%2F~1heroes~1%7Bhero_id%7D~1durations%2Fget)
            5.  heroes/{hero_id}/players        (https://docs.opendota.com/#tag/heroes%2Fpaths%2F~1heroes~1%7Bhero_id%7D~1players%2Fget)
            6.  heroes/{hero_id}/itemPopularity (https://docs.opendota.com/#tag/heroes%2Fpaths%2F~1heroes~1%7Bhero_id%7D~1itemPopularity%2Fget)
        """
        req_list_allowed = ['matches', 'matchups', 'durations', 'players', 'itemPopularity']
        params = {
            'hero_id': hero_id
        }
        params = self.api_auth_check(params)

        if not hero_id:
            req_name = None
            url = '{}{}'.format(self.base_url, 'heroes')
            response = requests.get(url)
        else:
            if req_name == None:
                url = '{}heroes/{}'.format(self.base_url, hero_id)
                response = requests.get(url, params=params)
            elif req_name not in req_list_allowed:
                return 'Вызываемый метод не из списка: {}'.format(req_list_allowed)
            else:
                url = '{}heroes/{}/{}'.format(self.base_url, hero_id, req_name)
                response = requests.get(url, params=params)
        result = response.json()
        return result

    def matches(self, match_id):
        """ Функция возвращает данные о матче по его match_id
        Описание: (https://docs.opendota.com/#tag/matches%2Fpaths%2F~1matches~1%7Bmatch_id%7D%2Fget)
        Параметры:
        --- match_id: ID матча
        """
        url = '{}matches/{}'.format(self.base_url, match_id)
        response = requests.get(url)
        result = response.json()
        return result

    def constants(self, resource=None):
        """ Функция возвращает константы API OpenDota
        Для получения списка констант, необходимо вызвать функцию без указания параметров
        Описание: (https://docs.opendota.com/#tag/constants%2Fpaths%2F~1constants~1%7Bresource%7D%2Fget)
        Параметры:
        --- resource: Наименование списка констант
        """
        if resource == None:
            url = '{}{}'.format(self.base_url, 'constants')
            response = requests.get(url)
        else:
            url = '{}constants/{}'.format(self.base_url, resource)
            response = requests.get(url)
        result = response.json()
        return result

    def explorer(self, sql):
        """ Функция возвращает результат от произвольного SQL-запроса к БД Opendota
        Описание: (https://docs.opendota.com/#tag/explorer%2Fpaths%2F~1explorer%2Fget)
        Параметры:
        --- sql: Произвольный текстовый sql выражение
        """
        params = {
            'sql': sql
        }
        params = self.api_auth_check(params)
        url = '{}explorer'.format(self.base_url)
        response = requests.get(url, params=params)
        result = response.json()['rows']
        return result

    def job_request(self, job_id, req_type='get'):
        """ Функция отправляет запрос на парсинг матча и возвращает результат парсинга матча
        Описание: (https://docs.opendota.com/#tag/request)
        Параметры:
        --- job_id:
            Если GET запрос, то необходимо передать match_id матча, который необходимо распарсить
            Если POST запрос, то необходимо передать job_id
        --- req_type: Выбор типа выполняемого запроса
        :return:
        """
        url = '{}request/{}'.format(self.base_url, job_id)
        if req_type == 'get':
            response = requests.get(url)
        elif req_type == 'post':
            response = requests.post(url)
        else:
            return 'Можно выполнять только GET и POST запросы'
        result = response.json()
        return result