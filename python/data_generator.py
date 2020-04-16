from faker import Faker


class DataGenerator:

	def get_full_names(self, num_names):
		fake = Faker()
		names = []
		for i in range(num_names):
			names.append(fake.name())
		return names


	def get_fake_future_dates(self, num_dates):
		fake = Faker()
		dates = []
		for i in range(num_dates):
			dates.append(fake.date_this_year(
				before_today=False,
				after_today=True))
		return dates


	def get_fake_past_dates(self, num_dates):
		fake = Faker()
		dates = []
		for i in range(num_dates):
			dates.append(fake.date_this_year(
				before_today=True,
				after_today=False))
		return dates


	def get_decimals(self, precision, scale, num_amts):
		fake = Faker()
		decimals = []
		digits_before_decimal = precision - scale
		to_numerify = "{}.{}".format(
			"#" * digits_before_decimal,
			"#" * scale)
		for i in range(num_amts):
			decimals.append(fake.numerify(text=to_numerify))
		return decimals


	def get_company_names(self, num_names):
		fake = Faker()
		names = []
		for i in range(num_names):
			names.append(fake.company.company())
		return names


	def get_fake_words(self, num_words, word_list, uniq=True):
		fake = Faker()
		try:
			words = fake.words(
				nb=num_words,
				ext_word_list=word_list,
				unique=uniq)
			return words
		except ValueError as e:
			print("ERROR: {}".format(e))


	def get_random_element(self,elements_list):
		fake = Faker()
		return fake.random_element(elements=elements_list)


	def get_transaction_description(self, transaction_id_length):
		fake = Faker()
		company = "{} {}".format(
			fake.company(),
			fake.company_suffix())
		transaction_id = str(fake.random_number(
			digits=transaction_id_length))
		date = self.get_fake_past_dates(1)[0].strftime('%Y/%m/%d')
		desc = "{} {} {} {}".format(
			company.upper(),
			transaction_id,
			date,
			company.title())
		return desc



	def get_random_titles(self, num_titles):
		fake = Faker()
		titles = []
		for i in range(num_titles):
			titles.append(fake.sentence(4)[0:-1].title())
		return titles






