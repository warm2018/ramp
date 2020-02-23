

SET = ['a3i_CAV.6', 'a3i_CAV.9', 'a3i_HV.7', 'a4i_CAV.12', 'a3i_CAV.11', 'a4i_HV.8', 'a4i_HV.9', 'a3i_HV.8', 'a3i_CAV.12', 'a4i_HV.10', 'a3i_HV.9', 'a3i_CAV.13', 'a3i_HV.10', 'a3i_HV.11', 'a3i_HV.12', 'a3i_CAV.14', 'a3i_CAV.15', 'a3i_HV.13', 'a3i_HV.14', 'a3i_HV.15']

def find_sequence(lane_result):
	CAV_set = []; HV = [0]; CAV_total = []; HV_total = [];
	count1 = 0; count2 = 0;
	for member in lane_result:
		if member.find('CAV') != -1:
			count2 = 0
			CAV_set.append(member)
			if count1 == 0:
				HV_total.append(HV)
				count1 = 1
		else:
			count1 = 0
			if count2 == 0:
				CAV_total.append(CAV_set)
				CAV_set = []
				count2 = 1
			HV = [member]

	topology = []	
	length = len(HV_total)
	print(length)
	for x,y in zip(HV_total,CAV_total[-length:]):
		if x == [0]:
			z = y
		else:
			z = x + y
		topology.append(z)

	return topology
## if the first member is CAV, CAV_total[0] == []
## if the first member is HV, H_total[]

if __name__ == '__main__':
	topology = find_sequence(SET)
	print(topology)